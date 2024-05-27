
$('.card').on('click', function () {
	var postImageSrc = $(this).find('.card-img').attr('src');
	var postLikesCount = $(this).find('.post-likes').html();
	var postCommentsCount = $(this).find('.card-overlay p').html();
	var modalContent = `
          <img src="${postImageSrc}" class="modal-img" alt="Post Image">
          <div class="modal-post-details">
              <p>${postLikesCount}</p>
              <p>${postCommentsCount}</p>
          </div>
      `;
	$('#modalBody').html(modalContent);
	$('#postModal').modal('show');
});