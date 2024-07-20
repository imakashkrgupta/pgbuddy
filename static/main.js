//--------------SEARCH CONTROL-------------------------------//
function price_range_input() {
    let price_range_val = document.getElementById("price_range").value;
    price_range_val = price_range_val * 1000;
    if (price_range_val == 10000) {
        document.getElementById("price_range_output_id").innerHTML = price_range_val + " " + "Rs" + "+";
    }
    else {
        document.getElementById("price_range_output_id").innerHTML = price_range_val + " " + "Rs";
    }

}
function distance_range_input() {
    let distance_range_val = document.getElementById("distance_range").value;
    distance_range_val = distance_range_val * 100;
    if (distance_range_val == 1000) {
        document.getElementById("distance_range_output_id").innerHTML = distance_range_val + " " + "m" + "+";
    }
    else {
        document.getElementById("distance_range_output_id").innerHTML = distance_range_val + " " + "m";
    }

}
/*--------------------------------------------------*/
//--------------NAV BAR-------------------------------//
let nav_menu_click_count = 1;
function nav_menu_clicked() {
    if (nav_menu_click_count % 2 != 0) {
        document.getElementById("navlinks_id").style.display = "block";
        document.getElementById("navlogo_id").style.display = "none";
        document.getElementById("search_bar_id").style.display = "none";
        nav_menu_click_count++;
    }
    else if (nav_menu_click_count % 2 == 0) {
        document.getElementById("navlinks_id").style.display = "none";
        document.getElementById("navlogo_id").style.display = "block";
        document.getElementById("search_bar_id").style.display = "block";
        nav_menu_click_count++;
    }
}
/*--------------------------------------------------*/
/*/////////*--------------SLIDER IMAGES-------------*////////////*/
let slider_img_counter = 1;
function right_slider_img() {
    let slider_img = document.getElementsByClassName("slider_img");
    for (let i = 0; i < slider_img.length; i++) {
        slider_img[i].style.display = "none";
    }
    slider_img_counter++;
    if (slider_img_counter > 3) {
        slider_img_counter = 1;
    }
    document.getElementById("slider_img" + slider_img_counter).style.display = "block";
}
function left_slider_img() {
    let slider_img = document.getElementsByClassName("slider_img");
    for (let i = 0; i < slider_img.length; i++) {
        slider_img[i].style.display = "none";
    }
    slider_img_counter--;
    if (slider_img_counter < 1) {
        slider_img_counter = 3;
    }
    document.getElementById("slider_img" + slider_img_counter).style.display = "block";
}
/*--------------------------------------------------*/
/*--------------------OWNER NAV-----------------*/
let owner_nav_menu_click_count = 1;
function owner_nav_btn_clicked() {
    if (owner_nav_menu_click_count % 2 != 0) {
        document.getElementById("owner_nav_id").style.display = "block";
        owner_nav_menu_click_count++;
    }
    else if (owner_nav_menu_click_count % 2 == 0) {
        document.getElementById("owner_nav_id").style.display = "none";
        owner_nav_menu_click_count++;
    }
}
/*--------------------------------------------------*/
/*----------------------REMOVING THE MESSAGES----------------------*/
function message_remove() {
    document.getElementById("messages_ul_id").style.display = "none";
}
/*---------------------------------------------------------------*/

/*------------------------EDITING OWNER BASIC DETAILS------------------*/
function owner_detail_edit() {
    //Removing Readyonly property from the input fields
    const collection = document.getElementsByClassName("owner_details_edit_input");
    for (let i = 0; i < collection.length; i++) {
        if (i == 0) {
            collection[i].focus();
            collection[i].setSelectionRange(collection[i].value.length, collection[i].value.length);
        }
        collection[i].readOnly = false;
    }

    document.getElementById("owner_detail_edit_btn_id").style.display = "none";
    document.getElementById("owner_detail_save_btn_id").style.display = "block";
}
/*---------------------------------------------------------------------*/
/*----------------------------DELETE POST-------------------------*/
function post_delete_btn_clicked(id) {
    Swal.fire({
        title: "Are you sure?",
        text: "You want to delete this post permanently?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!"
    }).then((result) => {
        if (result.isConfirmed) {
            setTimeout(function () {
                window.location.href = `delete-post/${id}`;
            }, 500);
        }
    });
}
/*----------------------------------------------------------------------*/
/*-----------------EDIT SELECTION option (Edit-Post Page)------------------*/
function select_edit_selection_opt(college, pgfor) {
    // alert(college)
    // alert(pgfor)
    document.getElementById("pgfor_select_id").value = pgfor;
    document.getElementById("add-room-select_id").value = college;
}

/*----CHCEKING NEW FILE UPLOADED to render it to show the new image sample----------------*/

// function check_file_uploaded(input){
//     /*-Removing the stored images from localstorage---------------*/
//     // localStorage.removeItem("uploadedFile");
//     /*-------------------------------------------*/
//     // const file = input.files[0]; // Get the first file from the FileList object
//     // console.log(file.name)
//     // -------------------------
//     // if (file) {
//     //     const reader = new FileReader();
//     //     reader.onload = function(event) {
//     //       const fileData = event.target.result;
//     //       localStorage.setItem('uploadedFile', fileData);
//     //       displayFileInfo(file);
//     //     };
//     //     reader.readAsDataURL(file);
//     //   }
//     // ----------------------------------------
//     // document.getElementById("edit_post_img_sample_id1").style.backgroundImage=`url('${localStorage.getItem('uploadedFile')}')`;

//     /*-Removing the stored images from localstorage---------------*/
//     // localStorage.removeItem("uploadedFile");
//     /*----------------------------------------*/
//     // const file = input.files[0]; // Get the first file from the FileList object
//     // if (file) {
//     //   const reader = new FileReader();
//     //   reader.onload = function(event) {
//     //     const fileData = event.target.result;
//     //     localStorage.setItem('uploadedFile', fileData);
//     //     // Call the displayFileInfo function
//     //     displayFileInfo(file);
//     //   };
//     //   reader.readAsDataURL(file);
//     //   document.getElementById("edit_post_img_sample_id1").style.backgroundImage=`url('${localStorage.getItem('uploadedFile')}')`;
//     // } else {
//     // //   document.getElementById('fileInfo').innerHTML = 'No file selected';
//     // }
// }

/*----------------------------------------------------------------------*/

function check_file_uploaded(evt, id) {

    var tgt = evt.target || window.event.srcElement,
        files = tgt.files;

    // FileReader support
    if (FileReader && files && files.length) {
        var fr = new FileReader();
        fr.onload = function () {
            document.getElementById(id).style.backgroundImage = `url("${fr.result}")`;
        }
        fr.readAsDataURL(files[0]);
    }

    // Not supported
    else {
        // fallback -- perhaps submit the input to an iframe and temporarily store
        // them on the server until the user's session ends.
    }

}

/*---------------------SPEECH RECOG. FOR SEARCH--------------------------*/
function speechrecog() {
    console.log("yep listening...")
    // document.getElementById("output").innerHTML = "Loading text...";
    var search_mic = document.getElementById('search_mic_id');
    var search_listening = document.getElementById('search_listening_id');
    var search_input = document.getElementById('search_input_id');
    // var action = document.getElementById('action');
    let recognization = new webkitSpeechRecognition();
    recognization.onstart = () => {
        // ------------VOICE SEARCH BUTTON SOUND--------
        const clickSound = document.getElementById('clickSound');
        clickSound.play();
        // --------------------------------
        search_mic.style.display="none";
        search_listening.style.display="flex";
        search_input.placeholder="Listening...";
        // action.innerHTML = "Listening...";
    }
    recognization.onresult = (e) => {
        var transcript = e.results[0][0].transcript;
        search_mic.style.display="flex";
        search_listening.style.display="none";
        console.log(transcript);
        search_input.value = transcript;
    }
    recognization.onend = function() {
        console.log('Speech recognition service disconnected');
        search_mic.style.display="flex";
        search_listening.style.display="none";
        search_input.placeholder="search your college to find the nearest PGs";
    }
    recognization.start();
}

/*-----------------------------------------------------------------------*/