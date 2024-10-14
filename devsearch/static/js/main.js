// GET SEARCH FORM AND PAGE LINKS
let searchForm = document.querySelector("#searchForm");
let pageLinks = document.getElementsByClassName("page-link");

// ENSURE SEARCH FORM EXISTS
if (searchForm) {
  for (let i = 0; i < pageLinks.length; i++) {
    pageLinks[i].addEventListener("click", function (event) {
      event.preventDefault();

      // GET THE DATA ATTRIBUTE
      let page = this.getAttribute("data-page");

      // ADD THE HIDDEN SEARCH INPUT TO FORM
      searchForm.innerHTML += `<input value=${page} name="page" hidden/>`;

      // SUBMIT FORM
      searchForm.submit();
    });
  }
}
