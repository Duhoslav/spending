$(document).ready(function(){
   $(".nav-item").removeClass("active");
   const href = window.location.pathname;
   const current_nav_item = $(".nav-link[href= '"+ href +"']");
   current_nav_item.parent().addClass("active");
});