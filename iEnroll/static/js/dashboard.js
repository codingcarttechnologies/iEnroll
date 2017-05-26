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
         $.ajax({
            type: "POST",
            url: "/deleteUser/",
            data: JSON.stringify(params),
            contentType: "application/json",
            success: function(res) {
                if (res == 'success') {
                    $.ajax({
                            url:'/update_table/',
                            type:'POST',
                            success:function(res){
                                $('.ajax_table').html(res)
                            }
                        });
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
    var new_tracking ='';
    var new_email = '';
    $('.edit_user').click(function(){
        $('#edit_fname').val($(this).attr('data-fname'));
        $('#edit_lname').val($(this).attr('data-lname'));
        $('#edit_email').val($(this).attr('data-email'));        
        $('#editModal').modal('show');        
        new_fname = $('#edit_fname').val();
        new_lname = $('#edit_lname').val();
        new_email = $('#edit_email').val();
        new_status = $(this).attr('data-status')
        new_tracking = $(this).attr('data-tracking')
        current_user = $(this).attr('data-id')
    })
    /*Edit a user data*/
    $('#edit_fname').on('change',function(){
        new_fname = $('#edit_fname').val();
    })
    $('#edit_lname').on('change',function(){
        new_lname = $('#edit_lname').val();
    })
    $('#edit_email').on('change',function(){
        new_email = $('#edit_email').val();
    })
    $('#edit_status').on('change', function(){
        new_status = $( "#edit_status option:selected" ).val();
    });
    $('#edit_tracking').on('change', function(){
        new_tracking = $( "#edit_tracking option:selected" ).val();
    });
    $('#confirm_edit').click(function(){

       
        if((new_fname != '') || (new_lname != '') || (new_status != '') || (new_tracking != '') 
            || (new_email != '') ){
            params = {
                'user_id': current_user,
                'new_fname':new_fname,
                'new_lname':new_lname,
                'new_status':new_status,
                'new_tracking':new_tracking,
                'new_email':new_email
                }
            $.ajax({
                type: "POST",
                url: "/updateUser/",
                data: JSON.stringify(params),
                contentType: "application/json",
                success: function(res) {
                    if (res == 'success') {
                        $('#editModal').modal('hide');        
                        $.ajax({
                            url:'/update_table/',
                            type:'POST',
                            success:function(res){
                                $('.ajax_table').html(res)
                            }
                        })
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

