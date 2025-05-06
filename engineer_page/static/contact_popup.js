const modal = document.getElementById("contactModal");
const btn = document.getElementById("openModal");
const btn2 = document.getElementById("openModal2");
const span = document.getElementsByClassName("close")[0];

const open_contacts = function(event) {
  event.preventDefault();
  modal.style.display = "block";
}
btn.onclick = open_contacts;
btn2.onclick = open_contacts;

span.onclick = function() {
  modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target === modal) {
    modal.style.display = "none";
  }
}