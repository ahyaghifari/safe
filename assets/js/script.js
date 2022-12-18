$(document).ready(function () {
  //SLIDER HOME
    var slider = tns({
      container: ".my-slider",
      items: 1,
      autoplay: true,
      controls: false,
      autoplayButtonOutput: false,
    });

  //NAV MENU
  $(".nav-toggle").click(function (e) {
    e.preventDefault();
    $("#nav-header").toggleClass("nav-anim");
  });

  // AOS
  AOS.init({
    duration: 1000,
    once: true,
  });

    $('.close-announ').click(function () {
        $('#dynamic-announcement').remove();
    });


});
