$(document).ready(function () {

    //SLIDER HOME
    if($('.my-slider').length) {    
        var slider = tns({
            container: '.my-slider',
            items: 1,
            autoplay: true,
            controls: false,
            autoplayButtonOutput: false
        })
    }    
    
    //NAV MENU
    $('.nav-toggle').click(function (e) { 
        e.preventDefault();
        $('#nav-header').toggleClass('nav-anim');
    });

    //IMAGE PREVIEW
    if ($('.form-menu div #id_gambar').val() != '') {
        $('#image-preview img').attr('src', $('.form-menu div #id_gambar').val())
    }

    $('.form-menu div #id_gambar').keyup(function (e) { 
        $('#image-preview img').attr('src', $(this).val())
    });

    // CLOSE MESSAGE CONFITRMATION
    $('.close-message-btn').click(function () {
        $('.messages').remove(); 
    });

    $('#delete-menu-form').submit(function (e) {
        e.preventDefault();        
        var id = $('.delete-btn').attr('id');
        
        Swal.fire({
           html: '<span class="text-cok">Yakin ingin menghapus '
                + id + '</span>',
            showCancelButton: true,
            target: 'main',
            color: '#171717',
            cancelButtonText: 'Tidak',
            confirmButtonText: 'Ya',
            background: '#f5f5f5',
            cancelButtonColor: '#171717',
            confirmButtonColor: '#800000',
        }).then((result) => {
            if (result.isConfirmed) {
                $.ajax({
                    type: "POST",
                    url: "/menu/delete/",
                    data: {
                        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                        nama: id,
                    },
                    dataType: "json",
                    success: function (response) {
                        if (response.confirm = '200') {
                            window.location.replace('/menu')
                        }   
                    }
                });
            } else {
                return false;
            }
        })

    });

    // AOS
    AOS.init({
        duration: 1000,
        once: true
    });
    

    // if ($('#id_tanggal_pemesanan').val() != '') {
    //         console.log("a");
    // }

    $('#id_tanggal_pemesanan').change(function () { 
        date = $(this).val()

        $.ajax({
            type: "GET",
            url: "/reservasi/cek",
            data: {
                date : date
            },
            dataType: "json",
            success: function (response) {
                $('#order-date').html(response.message)
                if (response.response == "200") {
                    $('#order-date').addClass('bg-green-600')
                    $('#order-date').removeClass('bg-red-600');
                    $('.reservation-btn').removeAttr('disabled')
                }else if (response.response == "400") {
                    $('#order-date').addClass('bg-red-600')
                    $('#order-date').removeClass('bg-green-600');
                    $('.reservation-btn').attr("disabled", true);
                }
            }
        });

    });

});