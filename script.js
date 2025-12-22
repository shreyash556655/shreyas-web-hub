const laptop = document.querySelector(".laptop-3d");

document.addEventListener("mousemove", (e) => {
  const x = (window.innerWidth / 2 - e.clientX) / 25;
  const y = (window.innerHeight / 2 - e.clientY) / 25;

  laptop.style.transform = `rotateY(${-x}deg) rotateX(${y}deg)`;
});
