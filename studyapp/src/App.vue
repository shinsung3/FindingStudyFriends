<template>
  <v-app>
    <v-app-bar
      app
      color="black"
    >
      <div class="d-flex align-center">
        <v-toolbar-title class="headline" style="color:white;">
          Study <v-span style="color:red">Group</v-span>
        </v-toolbar-title>
      </div>

      <v-spacer></v-spacer>

      <v-div id="toolBarPadding">
        <v-btn icon color="white">
          <v-span>HOME</v-span>
        </v-btn>
      </v-div>
      <v-div id="toolBarPadding">
        <v-btn icon color="white">
          <v-span>LOGIN</v-span>
        </v-btn>
      </v-div>
      <v-div id="toolBarPadding">
        <v-btn icon color="white">
          <v-span>STUDY</v-span>
        </v-btn>
      </v-div>
      <v-div id="toolBarPadding">
        <v-btn icon color="white">
          <v-icon>mdi-magnify</v-icon>
        </v-btn>
      </v-div>

      <v-btn
        href="https://github.com/vuetifyjs/vuetify/releases/latest"
        target="_blank"
        text
        color="white"
      >
        <span class="mr-2"></span>
        <v-icon>mdi-open-in-new</v-icon>
      </v-btn>
    </v-app-bar>
    <v-content>
      <section id="hero">
        <v-row no-gutters>
          <v-img
            style="opacity:0.85"
            :min-height="'calc(100vh - ' + $vuetify.application.top + 'px)'"
            src="https://images.unsplash.com/photo-1487017159836-4e23ece2e4cf?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1951&q=80"
          >
            <v-theme-provider dark>
              <v-container fill-height>
                <v-row
                  align="center"
                  class="white--text mx-auto"
                  justify="center"
                >
                  <v-col
                    class="text-center"
                    cols="12"
                    tag="h1"
                    style="color:red;"
                  >

                    <br>
                    <span
                      class="font-weight-black display-2"
                    >
                      Finding Study Group
                    </span>
                  </v-col>
                  <v-col
                    class="white--text text-center"
                    cols="12"
                    tag="h1"
                  >
                    <span
                      class="display-3 font-weight-black"
                    >
                      나에게 딱 알맞는 스터디 그룹 찾기
                    </span>

                  </v-col>

                  <v-btn
                    class="align-self-end"
                    fab
                    outlined
                    @click="$vuetify.goTo('#study-card')"
                  >
                    <v-icon>mdi-chevron-double-down</v-icon>
                  </v-btn>
                </v-row>
              </v-container>
            </v-theme-provider>
          </v-img>
        </v-row>
      </section>
    </v-content>
    <v-main>
      <HelloWorld/>
    </v-main>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';

export default {
  name: 'App',

  components: {
    HelloWorld,
  },

  data: () => ({
    //
  }),
};
</script>
<style scoped>
  #toolBarPadding{
    padding:10px;
  }
</style>
