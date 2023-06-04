/* menü stick stil kodları*/
window.addEventListener("scroll", function(){
    var nav = document.querySelector("nav");
    nav.classList.toggle("sticky", window.scrollY > 0);
});
//scrollreveal script kodu
        
          ScrollReveal().reveal('.card',{delay: 150});
          ScrollReveal().reveal('.alt-1',{delay: 180});
//scrollreveal script kodu


//aos kütüphanesi script kodu

  AOS.init();
//aos kütüphanesi script kodu


/*daktilo efekt kodları*/
$(function(){
     $('#t').t({
        caret:'<span style="color: tomato;">\u2582',
        beep:false,
        blink_perm:true,
        speed:140,
        repeat: 0,
        tag:'span',
    });
  
});
$(function(){
    $('#u').t({
       caret:'<span style="color: tomato;">\u2582',
       beep:false,
       blink_perm:true,
       speed:140,
       repeat: 0,
       tag:'span',
   });
 
});

// back to top
var btn = $('#button');

$(window).scroll(function() {
  if ($(window).scrollTop() > 300) {
    btn.addClass('show');
  } else {
    btn.removeClass('show');
  }
});

btn.on('click', function(e) {
  e.preventDefault();
  $('html, body').animate({scrollTop:0}, '300');
});