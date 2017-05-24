$(document).ready(function(){
        $('#example').DataTable();
    });

/* Delete a record */
$('.delete_user').click(function(){

    if( confirm("Are you sure to delete?") == true){
       var user_id = $(this).attr('data-id');
       params = {
            'user_id': user_id,
            }
        console.log('params',params)
         $.ajax({
            type: "POST",
            url: "/deleteUser/",
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function(res) {
                if (res == 'success') {
                    window.location.href='/dashboard/'
                } else {
                    console.log('error')
                }
            }
        });
    }
});

    /* Open Bootstrap edit modal*/
    var new_fname = '';
    var new_lname = '';
    var new_status = '';
    var current_user = '';
    $('.edit_user').click(function(){
        $('#edit_fname').val($(this).attr('data-fname'));
        $('#edit_lname').val($(this).attr('data-lname'));
        $('#edit_status').val($(this).attr('data-status'));
        $('#editModal').modal('show');
        new_fname = $('#edit_fname').val();
        new_lname = $('#edit_lname').val();
        new_status = $('#edit_status').val();
        current_user = $(this).attr('data-id')
    })

    /*Edit a user data*/
    $('#edit_fname').on('change',function(){
        new_fname = $('#edit_fname').val();
    })
    $('#edit_lname').on('change',function(){
        new_lname = $('#edit_lname').val();
    })
    $('#edit_status').on('change',function(){
        new_status = $('#edit_status').val();
    })
    $('#confirm_edit').click(function(){

        console.log('here','new_fname',new_fname,'new_lname',new_lname,'new_status',new_status,'user',current_user)
        if((new_fname != '') || (new_lname != '') || (new_status != '')){
            params = {
                'user_id': current_user,
                'new_fname':new_fname,
                'new_lname':new_lname,
                'new_status':new_status,
                }
            console.log('params',params)
            $.ajax({
                type: "POST",
                url: "/updateUser/",
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function(res) {
                    if (res == 'success') {
                        console.log('success')
                        window.location.href='/dashboard/'
                    } else {
                        console.log('error')
                    }
                }
            });
        }else{
            alert('Please fill all the fields')
        }
    })


$(function() 
   {
        $('.status').bind('keyup input',function()
        {       
            if (this.value.match(/[^a-zA-Z áéíóúÁÉÍÓÚüÜ]/g)) 
            {
                this.value = this.value.replace(/[^a-zA-Z áéíóúÁÉÍÓÚüÜ]/g, '');
            }
        });
    });

   $(".names").keypress(function(e) {
    if(e.which < 97 /* a */ || e.which > 122 /* z */) {
        e.preventDefault();
    }
});

// addNewUser  
$('#addNewUser').on('click',function(){
    $('#AddUserModal').modal('show');
    $('#confirm_add').click(function(){

        var fname = $('#add_fname').val();
        var add_lname = $('#add_lname').val();
        var add_status = $('#add_status').val();

        params = { 'fname':fname,'add_lname':add_lname,'add_status':add_status}

        $.ajax({
            type: "POST",
            url: "/addUser/",
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function(res) {
                
            }
        })

    });
});

//

