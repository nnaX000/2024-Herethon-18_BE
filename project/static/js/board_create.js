// 개발 기간 드롭다운
function toggleDropdown() {
  document
    .querySelector(".board-create-dropdown-content")
    .classList.toggle("board-create-dropdown-show");
}

function selectOption(option, inputId, buttonSelector) {
  event.preventDefault(); // 기본 동작 방지
  document.querySelector(buttonSelector).innerHTML = option;
  document.getElementById(inputId).value = option; // 값 저장
  toggleDropdown();
}

// 참여 인원 드롭다운
function toggleDropdown2() {
  document
    .querySelector(".board-create-dropdown-content2")
    .classList.toggle("board-create-dropdown-show");
}

function selectOption2(option, inputId, buttonSelector) {
  event.preventDefault(); // 기본 동작 방지
  document.querySelector(buttonSelector).innerHTML = option;
  document.getElementById(inputId).value = option; // 값 저장
  toggleDropdown2();
}

// 사용 언어 드롭다운
function toggleDropdown3() {
  document
    .querySelector(".board-create-dropdown-content3")
    .classList.toggle("board-create-dropdown-show");
}

function selectLanguage(language) {
  event.preventDefault(); // 기본 동작 방지
  const selectedLanguagesInput = document.getElementById("language_input");
  const selectedLanguages = selectedLanguagesInput.value
    ? selectedLanguagesInput.value.split(",")
    : [];

  if (!selectedLanguages.includes(language)) {
    selectedLanguages.push(language);
    selectedLanguagesInput.value = selectedLanguages.join(",");

    const languageBox = document.createElement("div");
    languageBox.className = "languageBox";
    languageBox.innerText = language;

    document
      .getElementById("board-create-selected-languages")
      .appendChild(languageBox);
  }

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

// 전역 클릭 이벤트 핸들러 - 드롭다운 닫기
window.onclick = function (event) {
  if (
    !event.target.matches(".board-create-dropdown-btn") &&
    !event.target.matches(".board-create-dropdown-btn2") &&
    !event.target.matches(".board-create-dropdown-btn3")
  ) {
    const dropdowns = document.getElementsByClassName(
      "board-create-dropdown-content"
    );
    for (let i = 0; i < dropdowns.length; i++) {
      const openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("board-create-dropdown-show")) {
        openDropdown.classList.remove("board-create-dropdown-show");
      }
    }

    const dropdowns2 = document.getElementsByClassName(
      "board-create-dropdown-content2"
    );
    for (let i = 0; i < dropdowns2.length; i++) {
      const openDropdown2 = dropdowns2[i];
      if (openDropdown2.classList.contains("board-create-dropdown-show")) {
        openDropdown2.classList.remove("board-create-dropdown-show");
      }
    }

    const dropdowns3 = document.getElementsByClassName(
      "board-create-dropdown-content3"
    );
    for (let i = 0; i < dropdowns3.length; i++) {
      const openDropdown3 = dropdowns3[i];
      if (openDropdown3.classList.contains("board-create-dropdown-show")) {
        openDropdown3.classList.remove("board-create-dropdown-show");
      }
    }
  }
};
