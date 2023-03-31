var slideIndex = 0;
function showNextSlide() {
    var slides = document.getElementsByClassName("slide");
    slides[slideIndex].style.display = "none";
    slideIndex = (slideIndex + 1) % slides.length;
    slides[slideIndex].style.display = "block";
  }
  setInterval(showNextSlide, 5000);

  var newpage = document.getElementById("m2")
  newpage.link("Plumbing Materials: All about Plumbing Pipe and Fittings (toplineindustries.in)")
