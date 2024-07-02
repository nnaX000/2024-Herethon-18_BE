document.querySelectorAll('.option').forEach(option => {
    option.addEventListener('click', function() {
        document.querySelectorAll('.option').forEach(opt => opt.classList.remove('selected'));
        this.classList.add('selected');
    });
});

function toggleInvitedList() {
    const invitedList = document.getElementById('invited-list');
    invitedList.style.display = invitedList.style.display === 'none' ? 'block' : 'none';
}