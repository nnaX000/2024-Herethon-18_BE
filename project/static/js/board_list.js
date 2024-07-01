document.addEventListener("DOMContentLoaded", function () {
  const boardPostBtn = document.querySelector(".board-post-btn");
  boardPostBtn.addEventListener("click", function () {
    window.location.href = "../html/board_create.html";
  });
});
