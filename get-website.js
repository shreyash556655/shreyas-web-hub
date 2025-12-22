function sendToWhatsApp() {
  let name = document.getElementById("name").value;
  let phone = document.getElementById("phone").value;
  let email = document.getElementById("email").value;
  let details = document.getElementById("details").value;

  let message =
    "📩 New Website Request%0A%0A" +
    "👤 Name: " + name + "%0A" +
    "📞 Phone: " + phone + "%0A" +
    "📧 Email: " + email + "%0A%0A" +
    "📝 Website Details:%0A" + details;

  let whatsappURL =
    "https://wa.me/17709073640?text=" + message;

  window.open(whatsappURL, "_blank");
}
