document.getElementById('settingToggleContainer').addEventListener('click', function () {
    let settingToggleContainer = this;
    let toggleButton = settingToggleContainer.querySelector('.setting-toggle-btn');
    if (settingToggleContainer.classList.contains('on')) {
        settingToggleContainer.classList.remove('on');
        toggleButton.textContent = '비동의';
        toggleButton.style.left = 'calc(100% - 87.4px + 2px)';
    } else {
        settingToggleContainer.classList.add('on');
        toggleButton.textContent = '동의';
        toggleButton.style.left = '-2px';
    }
});