// Git Practice - Main Script
"use strict";

document.addEventListener("DOMContentLoaded", () => {
  console.log("App loaded successfully!");

  const btn = document.querySelector(".btn-primary");
  if (btn) {
    btn.addEventListener("click", () => {
      alert("Hello from Git Practice!");
    });
  }
});

function formatDate(date) {
  return date.toISOString().split("T")[0];
}

function greet(name) {
  return `Welcome, ${name}!`;
}
