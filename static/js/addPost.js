$('#nextToSecondModal').click(function () {
            $('#createPostModal').modal('hide');
            $('#secondModal').modal('show');
            $('#imagePreviewSecondModal').attr('src', $('#imagePreview').attr('src'));
        });
        $('#backToFirstModal').click(function () {
            $('#secondModal').modal('hide');
            $('#createPostModal').modal('show');
        });
        $('#submitPost').click(function () {
            var formData = new FormData($('#postForm')[0]);
            var secondFormData = new FormData($('#secondModalForm')[0]);
            for (var pair of secondFormData.entries()) {
                formData.append(pair[0], pair[1]);
            }

            $.ajax({
                url: $('#postForm').attr('action'),
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                success: function (response) {
                    console.log(response);
                    $('#createPostModal').modal('hide');
                    $('#secondModal').modal('hide');
                },
                error: function (xhr, status, error) {
                    console.error(xhr.responseText);
                }
            });
        });

function previewImage(event) {
    var imagePreview = document.getElementById('imagePreview');
    var imageInput = event.target.files[0];
    if (imageInput && imageInput.type.startsWith('image')) {
        var reader = new FileReader();
        reader.onload = function () {
            imagePreview.src = reader.result;
            imagePreview.style.display = 'block';
        }
        reader.readAsDataURL(imageInput);
    } else {
        imagePreview.src = '#';
        imagePreview.style.display = 'none'; 
    }
}
document.getElementById('id_image').addEventListener('change', previewImage);


function updateImagePreview(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $("#imagePreviewSecondModal").attr("src", e.target.result);
        }

        reader.readAsDataURL(input.files[0]);
    }
}
$("#id_image").change(function () {
    updateImagePreview(this);
});
