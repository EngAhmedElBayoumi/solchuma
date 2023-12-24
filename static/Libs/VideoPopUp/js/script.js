(function($) {

	"use strict";





    








    /*------------------------------------------
        = POPUP YOUTUBE, VIMEO, GMAPS
    -------------------------------------------*/
//    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
//        type: 'iframe',
//        mainClass: 'mfp-fade',
//        removalDelay: 160,
//        preloader: false,
//        fixedContentPos: false
//    });



    /*------------------------------------------
        = POPUP VIDEO
    -------------------------------------------*/
//    if ($(".btnIconVideos").length) {
//        $(".btnIconVideos").on("click", function(){
//            $.fancybox({
//                href: this.href,
//                type: $(this).data("type"),
//                'title'         : this.title,
//                helpers     : {
//                    title : { type : 'inside' },
//                    media : {}
//                },
//
//                beforeShow : function(){
//                    $(".fancybox-wrap").addClass("gallery-fancybox");
//                }
//            });
//            return false
//        });
//    }

    if ($(".video-btn").length) {
        $(".video-btn").on("click", function () {
            $.fancybox({
                href: this.href,
                type: $(this).data("type"),
                'title': this.title,
                helpers: {
                    title: { type: 'inside' },
                    media: {}
                },

                beforeShow: function () {
                    $(".fancybox-wrap").addClass("gallery-fancybox");
                }
            });
            return false
        });
    }
    /*------------------------------------------
        = ACTIVE GALLERY POPUP IMAGE
    -------------------------------------------*/
    if ($(".popup-gallery").length) {
        $('.popup-gallery').magnificPopup({
            delegate: 'a',
            type: 'image',

            gallery: {
              enabled: true
            },

            zoom: {
                enabled: true,

                duration: 300,
                easing: 'ease-in-out',
                opener: function(openerElement) {
                    return openerElement.is('img') ? openerElement : openerElement.find('img');
                }
            }
        });
    }












})(window.jQuery);
