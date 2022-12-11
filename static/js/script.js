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
    

    //MODAL MENU
    $('.menu').on("click", function () {
        nama = $(this).children('p').attr('id')
        $.ajax({
            type: "GET",
            url: "/menu/detail",
            data: {
                menu: nama
            },
            dataType: "json",
            success: function (response) {
                menu = response.menu[0]
                
                $('#modal-menu-name').html(menu.nama)
                $('#modal-menu-image').attr('src', menu.gambar)
                $('#modal-menu-description').html(menu.deskripsi)
                $('#modal-menu-price').html(menu.harga)
                
                $('body').addClass('modal-open')
                $('#modal-overlay, #modal-menu').addClass('active')
            }
        });
    });
        
    var modal = document.getElementById('modal-overlay')
    var nav = document.getElementsByTagName('body')
    window.onclick = function (event) {
        if (event.target == modal) {
             $('body').removeClass('modal-open')
            $('#modal-overlay').removeClass('active')
            $('#modal-menu').removeClass('active')
        }
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

    // DELETE MENU FORM
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

    // CEK TANGGAL RESERVASI
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

    // NEWSLETTER
    $('#newsletter-form').submit(function (e) { 
        e.preventDefault();
        email = $('#newsletter-input').val()

        $.ajax({
            type: "POST",
            url: "/kontak/subscribe",
            data: {
                csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                email :  email
            },
            dataType: "json",
            success: function (response) {
                $('#newsletter-confirm').html(response.message)
                $('#newsletter-confirm').addClass('p-1')
                $('#newsletter-input').val('');
                if (response.responses == "200") {
                    $('#newsletter-confirm').addClass('bg-green-600')
                    $('#newsletter-confirm').removeClass('bg-red-600');
                } else if (response.responses == "400") {
                    $('#newsletter-confirm').addClass('bg-red-600')
                    $('#newsletter-confirm').removeClass('bg-green-600');
                }

            }
        });
        
    });
    $('#newsletter-input').keyup(function () {
        $('#newsletter-confirm').removeClass('p-1')
        $('#newsletter-confirm').html('')
    })


    //DELETE RESERVASI
     $('.delete-reservation-btn').click(function (e) {
        e.preventDefault();        
         var id = $(this).attr('id');
         console.log(id)
        
        Swal.fire({
           html: '<span class="text-cok">Yakin ingin menghapus reservasi ini ?</span>',
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
                    url: "/reservasi/delete/",
                    data: {
                        csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                        id: id,
                    },
                    dataType: "json",
                    success: function (response) {
                        if (response.confirm = '200') {
                            window.location.replace('/reservasi/all')
                        }   
                    }
                });
            } else {
                return false;
            }
        })

    });

});