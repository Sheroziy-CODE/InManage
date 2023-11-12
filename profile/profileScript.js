document.addEventListener('DOMContentLoaded', function() {

    var nameHeading = document.querySelector('.profile-info h1').textContent;
    document.getElementById('name').value = nameHeading;
});

document.getElementById('editProfile').addEventListener('click', function() {
    document.querySelectorAll('#profileForm input').forEach(input => {
        input.disabled = false;
    });

    document.getElementById('confirmEdit').style.display = 'block';

    this.style.display = 'none';
});

document.getElementById('profileForm').addEventListener('submit', function(event) {
    event.preventDefault();
    var nameValue = document.getElementById('name').value;
    document.querySelector('.profile-info h1').textContent = nameValue;

    document.querySelectorAll('#profileForm input').forEach(input => {
        input.disabled = true;
    });
    document.getElementById('confirmEdit').style.display = 'none';
    document.getElementById('editProfile').style.display = 'block';
});
