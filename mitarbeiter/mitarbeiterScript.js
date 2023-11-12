
document.querySelector('.add-staff').addEventListener('click', function() {
});

document.getElementById('addStaff').addEventListener('click', function() {
    document.getElementById('addStaffModal').style.display = 'block';
});

document.getElementById('closeModal').addEventListener('click', function() {
    document.getElementById('addStaffModal').style.display = 'none';
});

document.getElementById('addStaffForm').addEventListener('submit', function(event) {
    event.preventDefault();

    document.getElementById('addStaffModal').style.display = 'none';
});

window.onclick = function(event) {
    const modal = document.getElementById('addStaffModal');
    if (event.target == modal) {
        modal.style.display = 'none';
    }
};


