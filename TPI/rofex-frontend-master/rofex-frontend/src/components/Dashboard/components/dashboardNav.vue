<template>
    <nav class="navbar navbar-default">
        <div class="container-fluid navflex">
          <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
              <i class="fa fa-align-right"></i>
            </button>
            <a class="navbar-brand" href="#"><span class="main-color"></span></a>
          </div>
          <div class="collapse navbar-right" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
              <li class="dropdown">
                <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">My profile <span class="caret"></span></a>
                <ul class="dropdown-menu">
                  <li><a href="#"><i class="fa fa-user-o fw"></i> Cuenta</a></li>
                  <li><a href="#"><i class="fa fa-envelope-o fw"></i> Mensajes</a></li>
                  <li><a href="#"><i class="fa fa-question-circle-o fw"></i> Ayuda</a></li>
                  <li role="separator" class="divider"></li>
                  <li><router-link to='/'><i class="fa fa-sign-out"></i> Cerrar Sesion</router-link></li>
                </ul>
              </li>
              <li><a href="#"><i class="fa fa-comments"></i><span>23</span></a></li>
              <li><a href="#"><i class="fa fa-bell-o"></i><span>98</span></a></li>
              <li><a href="#"><i data-show="show-side-navigation1" class="fa fa-bars show-side-btn"></i></a></li>
            </ul>
          </div>
        </div>
      </nav>
</template>
<script>
import Vue from 'vue'
export default Vue.extend({
  name:'DashboardNav',
})
</script>