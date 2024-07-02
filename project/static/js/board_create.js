// 개발 기간 드롭다운
function toggleDropdown() {
  document
    .querySelector(".board-create-dropdown-content")
    .classList.toggle("board-create-dropdown-show");
}
function selectOption(option) {
  event.preventDefault(); // 기본 동작 방지
  document.querySelector(".board-create-dropdown-btn").innerHTML = option;
  toggleDropdown();
}
window.onclick = function (event) {
  if (!event.target.matches(".board-create-dropdown-btn")) {
    let dropdowns = document.getElementsByClassName(
      "board-create-dropdown-content"
    );
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("board-create-dropdown-show")) {
        openDropdown.classList.remove("board-create-dropdown-show");
      }
    }
  }
};

// 참여 인원 드롭다운
function toggleDropdown2() {
  document
    .querySelector(".board-create-dropdown-content2")
    .classList.toggle("board-create-dropdown-show");
}
function selectOption2(option) {
  document.querySelector(".board-create-dropdown-btn2").innerHTML = option;
  toggleDropdown2();
}
window.onclick = function (event) {
  if (!event.target.matches(".board-create-dropdown-btn2")) {
    let dropdowns = document.getElementsByClassName(
      "board-create-dropdown-content2"
    );
    for (let i = 0; i < dropdowns.length; i++) {
      let openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("board-create-dropdown-show")) {
        openDropdown.classList.remove("board-create-dropdown-show");
      }
    }
  }
};

// 사용 언어 드롭다운
function toggleDropdown3() {
  document
    .querySelector(".board-create-dropdown-content3")
    .classList.toggle("board-create-dropdown-show");
}
function selectLanguage(language) {
  let languageBox = document.createElement("div");
  languageBox.className = "languageBox";
  languageBox.innerText = language;
  // 중복 검사해야 됨
  document
    .getElementById("board-create-selected-languages")
    .appendChild(languageBox);
  toggleDropdown3();
}

// 파일 선택 기능
function boardFileInput() {
  document.getElementById("board-file-input").click();
}

// 파일 선택 시 파일명 표시
document
  .getElementById("board-file-input")
  .addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
      const fileName = file.name;
      const fileDisplay = document.getElementById("board-file-display");
      fileDisplay.innerText = fileName;
      fileDisplay.style.display = "block";
    }
  });
