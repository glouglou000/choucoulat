<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">

<section class="sectionPage" id="section_page_webcam2">
    <div class="Div"><!-- Top First Div -->

        <div class="divA" id="a1"><!-- Left Div -->
            <div id="buttons">
                <input type="button" id="response" onclick="phase1()">
                <input type="button" id="response2" onclick="phase2(0)">
                <input type="button" id="response3" onclick="phase3()">
            </div>
        </div>
        <div class="divB"></div>
        <div class="divC"></div>
 
    </div>


    <div class="Div">

        <div class="divA"><!-- Left Div -->
            <div id="formulaire">
                <form enctype="multipart/form-data" method="POST" action="">
                    {% csrf_token %}
                    {{ form.as_p }}
                    <input type="submit" value="Upload" id="upload"/>
                </form>
            </div>
        </div>

        <div class="divB">
            <div id="loading_eyes_section">
                <img src="static/home_composition/section3/images/loading_s3_p2_p3.gif" id="loading">
                <p>L O A D I N G ... <br>
                    Nous chargeons la vidéo, prenez le temps de visiter notre site, nous vous ferons signe
                </p>
            </div>
        </div>



        <div class="divC"></div>

 
    </div>


    <div class="Div">
        <div class="divA"><!-- Left Div --></div>
        <div class="divB"></div>
        <div class="divC"></div>

    </div>

</section>









<section class="sectionPage" id="section_page_webcam3">
    <div class="Div"><!-- Top First Div -->

        <div class="divA" id="a1"><!-- Left Div -->
            <div class="visualisation" id="visualisation1_eye_section">
                <h1>figure dlib</h1>
                <div id="video_application1"></div>
                <div id="eyetracking1"></div>
            </div>
        </div>

        <div class="divB">
            <div id="eyetracking2"></div>
        </div>


        <div class="divC">
            <div class="visualisation" id="visualisation2_eye_section">
                <h1>Main</h1>
                <div id="video_application"></div>
                <div id="eyetracking3"></div>
            </div>
        </div>

    </div>


    <div class="Div"><!-- Left Div -->
        <div class="divA">
            <div id="eyetracking4">
        </div>

        <div class="divB">
            <div id="eyetracking5"></div>
        </div>
        <div class="divC">
            <div id="eyetracking6"></div>
        </div>
    </div>


    <div class="Div">
        <div class="divA"><!-- Left Div -->
            <div id="eyetracking7"></div>
        </div>

        <div class="divB">

            <div id="eyetracking8"></div>
            enregistrer
            partager
        </div>

  
        <div class="divC">
            <div id="eyetracking9"></div>
        </div>
    </div>

</section>




















<style>
    .visualisation{
        width  : 100%;
        height : 100%;
        width  : 150.3%;
    }


    #section_page_webcam3{
        display : none;
        background         : #7BAABE;
        background-repeat  : no-repeat;
        background-position: center;
        background-size    : cover;
        opacity            : 0;
        -webkit-transition : opacity 2s;
        -moz-transition    : opacity 2s;
        -o-transition      : opacity 2s;
        transition         : opacity 2s;
        z-index            : 1;
    }
    #visualisation1_eye_section{
        position : absolute;
        float    : left;
    }
    #visualisation2_eye_section{
        position   : absolute;
        margin-left: -50%;
    }
    #buttons{
        display : none;
    }
    #loading{
        width : 20%;
    }
    #loading_eyes_section{
        margin-top :10%;
        opacity    :1;
        -webkit-transition: opacity 2s;
        -moz-transition   : opacity 2s;
        -o-transition     : opacity 2s;
        transition        : opacity 2s;
        display           :none;
    }
    #section_page_webcam2{
        background         : #7BAABE;
        background-repeat  : no-repeat;
        background-position: center;
        background-size    : cover;
        opacity            : 0;
        -webkit-transition : opacity 2s;
        -moz-transition    : opacity 2s;
        -o-transition      : opacity 2s;
        transition         : opacity 2s;
        z-index            : 1;
    }
    #formulaire{
        width       : 100%;
        height      : 100%;
        margin-left : 20%;
    }
</style>



<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/core.js"></script>

<script
  src="https://code.jquery.com/jquery-3.4.1.js"
  integrity="sha256-WpOohJOqMqqyKL9FccASB9O0KwACQJpFTUBLTYOVvVU="
  crossorigin="anonymous"></script>
  
<script>

    function phase1(){
        document.getElementById('formulaire').style.opacity = "0";
        document.getElementById('formulaire').style.display = "none";

        document.getElementById('loading_eyes_section').style.opacity = "1";
        document.getElementById('loading_eyes_section').style.display = "block";
    };


    function phase2(number){
        if (number == 0){
            interval = setInterval("verification_eye_application()", 5000)
        }else{
            clearInterval(interval);
            document.getElementById('loading_eyes_section').style.opacity = "0";
        }
    };

    function phase3(){
        console.log("functionnality's :", String(CHOICE_APPLICATION), "video name's : ", VIDEO_NAME)
          $.ajax({
              data:{"verification": "verification",
                    csrfmiddlewaretoken:'{{ csrf_token }}'
                   },
              type:"POST",
              url:"verify",
          })
          .done(function(data){
              if (data.error){
                  console.log("error phase3")
              }
              else{

                console.log("data tread : ", data["verification"], " on files numbers : ", data["number"])
                phase2(1);

                console.log("Phase4 in course ...")
                phase4();

             };
        });
    };



    function verification_eye_application(){

        console.log("Verification in course...")

          $.ajax({
              data:{"verification": "verification",
                    csrfmiddlewaretoken:'{{ csrf_token }}'
                   },
              type:"POST",
              url:"verify",
          })
          .done(function(data){
              if (data.error){
                  console.log("error verification")
              }
              else{

                console.log("data treat : ", data["verification"], " on files numbers : ", data["number"])

                if (data["verification"] > 1){

                    console.log("4 data has been treated, video can be send, popup in course...")
                    phase2(1);

                    console.log("Phase4 in course ...")
                    phase4();
                };
            };
        });
    };



    function face_appli(data){
        video = "<video width='100%' autoplay='true' controls muted loop><source src='" + data["video_situation1"] + "' type='video/mp4'></video>"
        document.getElementById('video_application').innerHTML = video;

        video1 = "<video width='100%' autoplay='true' controls muted loop><source src='" + data["video_situation2"] + "' type='video/mp4'></video>"
        document.getElementById('video_application1').innerHTML = video1;

    };

    function site_web_trakcer(data){
        video1 = "<video width='50%' autoplay='true' controls muted loop><source src='" + data["video"] + "' type='video/mp4'></video>"
        document.getElementById('eyetracking1').innerHTML = video1;

        video2 = "<video width='50%' autoplay='true' controls muted loop><source src='" + data["tracking1"] + "' type='video/mp4'></video>"
        document.getElementById('eyetracking2').innerHTML = video2;

        video3 = "<video width='50%' autoplay='true' controls muted loop><source src='" + data["tracking2"] + "' type='video/mp4'></video>"
        document.getElementById('eyetracking3').innerHTML = video3;

        img1 = "<img src='" + data["p1"] + "'>"
        document.getElementById('eyetracking4').innerHTML = img1;

        img2 = "<img src='" + data["p2"] + "'>"
        document.getElementById('eyetracking5').innerHTML = img2;

        img3 = "<img src='" + data["p3"] + "'>"
        document.getElementById('eyetracking6').innerHTML = img3;

        img4 = "<img src='" + data["p4"] + "'>"
        document.getElementById('eyetracking7').innerHTML = img4;

        img5 = "<img src='" + data["p5"] + "'>"
        document.getElementById('eyetracking8').innerHTML = img5;

        img6 = "<img src='" + data["p6"] + "'>"
        document.getElementById('eyetracking9').innerHTML = img6;
    };


    function phase4(){
        document.getElementById('section_page_webcam2').style.display = "none";

        document.getElementById('section_page_webcam3').style.display = "block";
        document.getElementById('section_page_webcam3').style.opacity = "1";


        console.log("Treatment video ... application in course : ", CHOICE_APPLICATION )


        $.ajax({
              data:{"application": CHOICE_APPLICATION,
                    "video_name":   VIDEO_NAME,
                    csrfmiddlewaretoken:'{{ csrf_token }}'
                   },
              type:"POST",
              url:"application",
          })
          .done(function(data){
              if (data.error){
                  console.log("error phase4")
              }
              else{
                console.log("video finish location : ", data["video_situation"])

                if (CHOICE_APPLICATION == "face"){
                    face_appli(data);
                }else if(CHOICE_APPLICATION == "eyes_tracking"){
                    site_web_trakcer(data);
                }else if(CHOICE_APPLICATION == "sleep"){

                    video1 = "<video width='50%' autoplay='true' controls muted loop><source src='" + data["video_situation"] + "' type='video/mp4'></video>"
                    document.getElementById('video_application').innerHTML = video1;

                    text = data["report"]
                    document.getElementById('video_application1').innerHTML = text;
                }


                

              };
        });
    };




    function treat_video_camera(name){

        console.log("Video in treating... verify phase in course...")
        document.getElementById("response2").click();


        $.ajax({
            data:{
                "video_name": name,
                csrfmiddlewaretoken:'{{ csrf_token }}'
            },
            type:"POST",
            url:"treat_video",
        })
        .done(function(data){
            if (data.error){
                {}
            }
            else{
                console.log("Video has been treat")
                document.getElementById('response3').click();
                phase2(1);
                alert_finish();
            };   
        });
    };



    var VIDEO_NAME = "";
    jQuery("form").on("submit", function(e){
        e.preventDefault();

        console.log("Uploading video in course...")

        var data = new FormData(this);

        $.ajax({
            data:data,
            cache: false,
            type:"POST",
            url:"uploading_file",
            processData:false,
            contentType:false,
          })
          .done(function(data){
              if (data.error){
                  {}
              }
              else{
                  console.log("Uploading video finish. Treating video in course...")
                  document.getElementById("response").click();
                  treat_video_camera(data["video_name"])
                  VIDEO_NAME = data["video_name"];
            };
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    };


    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    function alert_finish(){
        document.getElementById("alert").innerHTML = "Votre video eyes sections est peut etre visualisée !!!";
    };




</script>
