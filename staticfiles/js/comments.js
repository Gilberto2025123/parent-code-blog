document.addEventListener('DOMContentLoaded', function() {
  // Delete button logic only
  const deleteButtons = document.getElementsByClassName("btn-delete");
  const deleteModalElement = document.getElementById("deleteModal");
  const deleteConfirm = document.getElementById("deleteConfirm");
  let deleteModal = null;
  if (deleteModalElement) {
    deleteModal = new bootstrap.Modal(deleteModalElement);
  }

  for (let button of deleteButtons) {
    button.addEventListener("click", function() {
      let commentId = this.getAttribute("data-comment-id");
      let slug = this.getAttribute("data-slug");
      if (deleteConfirm) {
        deleteConfirm.href = `/blog/${slug}/delete_comment/${commentId}`;
      }
      if (deleteModal) {
        deleteModal.show();
      }
    });
  }
});
document.addEventListener('DOMContentLoaded', function() {
  // Get all the edit buttons
  const editButtons = document.getElementsByClassName("btn-edit");
  const commentText = document.getElementById("id_body");
  const commentForm = document.getElementById("commentForm");
  const submitButton = document.getElementById("submitButton");

  // Get delete buttons and modal
  const deleteModalElement = document.getElementById("deleteModal");
  const deleteConfirm = document.getElementById("deleteConfirm");
  const deleteButtons = document.getElementsByClassName("btn-delete");
  let deleteModal = null;
  if (!deleteModalElement) {
    console.error('Delete modal element with id "deleteModal" not found!');
  } else {
    deleteModal = new bootstrap.Modal(deleteModalElement);
  }
  if (!deleteConfirm) {
    console.error('Delete confirm button with id "deleteConfirm" not found!');
  }

  // Handle edit button clicks
  for (let button of editButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("comment_id");
      let commentContent = document.getElementById(`comment${commentId}`).innerText;
      commentText.value = commentContent;
      submitButton.innerText = "Update";
      commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
  }

  // Handle delete button clicks
  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let commentId = e.target.getAttribute("data-comment-id");
      let slug = e.target.getAttribute("data-slug");
      if (deleteConfirm) {
        deleteConfirm.href = `/blog/${slug}/delete_comment/${commentId}`;
      } else {
        console.error('Delete confirm button not found when trying to set href.');
      }
      if (deleteModal) {
        deleteModal.show();
      } else {
        console.error('Delete modal not found when trying to show.');
      }
    });
  }
});