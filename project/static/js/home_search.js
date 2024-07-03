document.addEventListener("DOMContentLoaded", () => {
  function addProjectBox(
    container,
    title,
    content,
    likeCount,
    commentCount,
    date,
    username
  ) {
    const projectBox = document.createElement("div");
    projectBox.className = "project-box";
    projectBox.innerHTML = `
            <div class="project-info">
                <div class="project-title">${title}</div>
                <div class="project-content">${content}</div>
                <div class="feedback-section">
                    좋아요 <p class="feedback-like">${likeCount}</p>
                    댓글 <p class="feedback-comment">${commentCount}</p>
                </div>
                <div class="project-date">${date}</div>
                <div class="project-username">${username}</div>
            </div>
            <div class="project-img">
                <img src="../img/person.png">
            </div>
        `;
    container.appendChild(projectBox);
  }

  const relevanceContainer = document.getElementById(
    "project-container-relevance"
  );
  const latestContainer = document.getElementById("project-container-latest");

  // Add projects to relevance container
  for (let i = 0; i < 5; i++) {
    addProjectBox(
      relevanceContainer,
      "Relevance Title " + (i + 1),
      "This is the description for relevance project " + (i + 1),
      8,
      3,
      "YYYY.MM.DD",
      "Username"
    );
  }

  // Add projects to latest container
  for (let i = 0; i < 5; i++) {
    addProjectBox(
      latestContainer,
      "Latest Title " + (i + 1),
      "This is the description for latest project " + (i + 1),
      8,
      3,
      "YYYY.MM.DD",
      "Username"
    );
  }

  const relevanceRadio = document.getElementById("relevance");
  const latestRadio = document.getElementById("latest");
  const labelRelevance = document.getElementById("label-relevance");
  const labelLatest = document.getElementById("label-latest");

  function updateLabelColors() {
    if (relevanceRadio.checked) {
      labelRelevance.style.color = "black";
      labelLatest.style.color = "gray";
    } else if (latestRadio.checked) {
      labelRelevance.style.color = "gray";
      labelLatest.style.color = "black";
    }
  }

  relevanceRadio.addEventListener("change", function () {
    if (relevanceRadio.checked) {
      relevanceContainer.style.display = "flex";
      latestContainer.style.display = "none";
      updateLabelColors();
    }
  });

  latestRadio.addEventListener("change", function () {
    if (latestRadio.checked) {
      relevanceContainer.style.display = "none";
      latestContainer.style.display = "flex";
      updateLabelColors();
    }
  });

  // 초기 색상 설정
  updateLabelColors();
});
