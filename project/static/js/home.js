        // 프로젝트 박스를 동적으로 생성하는 함수
        function createProjectBox(title, content) {
            const projectBox = document.createElement('div');
            projectBox.className = 'project-box';

            const img = document.createElement('img');
            img.src = '/img/person.png';
            img.alt = '프로젝트 이미지';

            const projectTitle = document.createElement('div');
            projectTitle.className = 'project-title';
            projectTitle.textContent = title;

            const projectContent = document.createElement('div');
            projectContent.className = 'project-content';
            projectContent.textContent = content;

            projectBox.appendChild(img);
            projectBox.appendChild(projectTitle);
            projectBox.appendChild(projectContent);

            return projectBox;
        }

        // 특정 섹션에 프로젝트 박스를 추가하는 함수
        function addProjectsToSection(sectionId, numProjects) {
            const container = document.getElementById(sectionId);
            for (let i = 1; i <= numProjects; i++) {
                const projectBox = createProjectBox(`프로젝트 제목 ${i}`, `프로젝트 설명 ${i}`);
                container.appendChild(projectBox);
            }
        }

        // 각 섹션에 15개의 프로젝트 박스를 추가
        addProjectsToSection('recent-projects', 15);
        addProjectsToSection('most-viewed-projects', 15);
        addProjectsToSection('popular-projects', 15);