# FindingStudyFriends
FindingStudyFriends - 스터디 친구 찾기 WEB 플랫폼

- Django
  - Successfully installed asgiref-3.3.4 django-3.2.3 pytz-2021.1 sqlparse-0.4.1
- 원하는 작업 내용.
  1. 일반적인 온라인 강의 사이트처럼 여러 스터디가 생성되어 있고 사용자가 원하는 스터디를 참여 신청하는 방식.
  2. 로그인 할 수 있는 사용자 계정을 생성하고, 로그인 시 사용자는 찜한 스터디, 참여한 스터디 목록을 보고 인증글을 작성 할 수 있습니다.
  3. 사용자가 직접 카테고리 별(어학, 취업, 공무원 및 전문시험, 기타 등)으로 필요에 맞게 스터디를 세부적으로 설정하여 생성할 수 있습니다. 생성된 스터디 에는 스터디 이름, 지역, 인원, 온 오프라인 체크, 카카오톡 오픈채팅 주소(?), 기타 정보 및 스터디 방식을 표시, 모집 마감 기한 및 스터디 기간을 표시할 예정입니다. 
  4. 생성된 스터디를 쉽게 찾을 수 있도록 지역, 온 오프라인 및 이름 별로 검색할 수 있습니다.
  5. 참여 인원이 다 차거나 작성자가 모집을 마감한 스터디는 신청한 스터디원들을 오픈 채팅방으로 안내하고, 내 스터디 목록에서 해당 스터디 정보와 스터디한 인증사진업로드 및 댓글을 다는 커뮤니티(?)기능.
  6. 추가적으로 필요에 따라 모집 기간이 임박한 스터디를 표시하거나 추천
  7. 관리자 계정이 필요한가? -> 사용자들 글 수정, 삭제 가능?, 정보보기같은 것?



- 필수 사항??
  - 웹페이지 만들어서 **[배포]**



- 데이터 베이스 (DB) 
  - 테이블
    - studyGroup
      - 제목(이름), 내용, 날짜(작성한 날짜), D- Day(앞단), 마감기한, 인원수, 카테고리, img링크(또는 랜덤하게), 오픈채팅방링크, on-off, 지역, 스터디 기간, 스터디이름
    - User
      - id, pw, email, 닉네임
    - MyPage
      - 참여한정보, 북마크해놓은정보(즐겨찾기)
    - User1 -> 외래키를 통해서 연결.

- 백엔드, 프론트엔드, 데이터베이스, 서버올리기(AWS)
  - 백엔드 파이썬 문법 잘 모르고,
  - 백엔드 django 도 모르고
    - 수업을 하면 -> 만들어와야 함.
  - 프론트엔드 어려울거같고
    - CSS 연동할 수 있게 다운받아서 하는 쪽으로 -> 안되면 그냥 HTML, CSS, js사용해서 만들기.



- migration

  ```
  CREATE TABLE "studyapp_studygroup" (
  	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  	"title" varchar(500) NOT NULL, 
  	"contents" varchar(1000000000) NOT NULL, 
  	"writeDay" datetime NOT NULL, 
  	"finalDate" date NOT NULL, 
  	"member" integer NOT NULL, 
  	"category" varchar(500) NOT NULL, 
  	"imgLink" varchar(500) NOT NULL, 
  	"kakaoLink" varchar(500) NOT NULL, 
  	"onOff" varchar(500) NOT NULL, 
  	"name" varchar(500) NOT NULL
  );
  COMMIT;
  ```

  

- 003 

  ```
  CREATE TABLE "new__studyapp_studygroup" (
  	"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  	"region" varchar(500) NULL, 
  	"title" varchar(500) NOT NULL, 
  	"contents" varchar(1000000000) NOT NULL, 
  	"writeDay" datetime NOT NULL, 
  	"finalDate" date NOT NULL, 
  	"member" integer NOT NULL, 
  	"category" varchar(500) NOT NULL,
      "imgLink" varchar(500) NOT NULL, 
      "kakaoLink" varchar(500) NOT NULL, 
      "onOff" varchar(500) NOT NULL, "name" varchar(500) NOT NULL
  );
  
  INSERT INTO "new__studyapp_studygroup" (
  	"id", "title", "contents", "writeDay", "finalDate", "member", "category", 	
  	"imgLink", "kakaoLink", "onOff", "name", "region"
  )
  
  SELECT "id", "title", "contents", "writeDay", "finalDate", "member", "category", "imgLink", "kakaoLink", "onOff", "name", NULL FROM "studyapp_studygroup";
  
  DROP TABLE "studyapp_studygroup";
  
  ALTER TABLE "new__studyapp_studygroup" RENAME TO "studyapp_studygroup";
  COMMIT;
  ```

  
