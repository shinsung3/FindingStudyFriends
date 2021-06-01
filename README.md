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

  



## Main Page

흐름: 사이트 방문시 사용자에게 보여지는 첫 메인화면이다. 

- [ ] 반응형 웹사이트이다. 
- [x] `왼쪽 위 상단에(nav-bar) [STUDYGROUP]로고글씨가 있고, 클릭시 Home으로 이동한다.` 
- [ ] 오른 쪽 위 상단에(nav-bar) [Home], [Study], [My Group], [Login], [검색창] 이 있다. 해당 메뉴 클릭시 그 페이지로 이동하며 해당 탭의 글씨 밑에 빨간 밑줄이 표시된다. 3. 화면을 아래로 스크롤해도 상단의 nav-bar는 유지된다. 4. 화면 크기가 줄어들면 오른쪽 상단이 [햄버거모양 버튼]으로 바뀌며 클릭 시   [Home], [Study], [My Group], [Login] 메뉴가 드롭다운으로 나타난다. 그리고, 햄버거모양버튼 왼쪽에 [검색창]이 있다. 4-1 [Login]완료 시 Login 글씨 대신 사람모양 아이콘으로 변경,my group탭이 보여진다. 또한, 해당 사람모양 아이콘 클릭시 [마이페이지]로 이동한다. 4-2[검색창] 에 입력된 단어 또는 문장이 [Study]페이지의 [스터디 제목]과[한줄소개글]과 비교하여 일치할 시 [study]페이지에서 해당 스터디 목록을 보여준다.  ->모든 페이지 적용 5. 헤더의 banner는 carousel으로 3개가 나타난다. 배경에는 사진이 약간 투명하게 있고, 첫번재는, 'FINDING STUDY GROUP' '나에게 딱 알맞는 스터디 그룹 찾기!'. 두번째는, 'FINDING STUDY FRIENDS' '함께할 스터디 친구를 구해보자!'. 세번째는, 'FINDING STUDY PARTNER' '종류별 스터디를 이곳에서 한번에 구하자!' 문구 표시. 4. body에는 기본적으로 '최신순'으로 스터디 목록 3개씩 2줄(총6개)가 보여진다.  5.body 우측상단에는 [전체보기]가 있고 클릭 시 [study]페이지로 화면이 이동된다. 6.회원이 사전에 게시글 [생성하기]했을 때 등록한 [사진],[카테고리],[제목],[한줄소개글], [생성날짜],[모집기간D-Day],[참여하기]버튼, [찜표시]:별모양이 표시된다. 6-1 [카테고리]는 [어학],[취업],[학습],[기타]로 이루어져 있고 각 카테고리별 고정 색상이 있다.(우측사진 둥근사각형에 초록,보라,주황안에 흰글씨 있는 디자인 참고) 6-2[찜표시]는 즐겨찾기 기능으로 처음에는 빈 별모양이 기본이며, 회원이 별모양 클릭시 빨간색별모양으로 바뀌며, [My Group]에서 [찜한스터디]카테고리에서 스터디 목록 확인할 수 있음. 6-3[모집기간D-Day]는 생성된 날짜에서 모집마감기한까지의 D-Day를 'D-3일'로 날짜 표시한다. 7.우측 하단에 [스터디 생성하기]버튼을 통해 [게시글세부사항작성]의 작성 팝업?창이 뜬다. 7-1 [스터디 생성하기]버튼 클릭시 로그인 여부확인을 하고, 로그인 되어있는 회원일 시 작성권한부여, 비회원일시 회원가입 페이지로 이동한다.

