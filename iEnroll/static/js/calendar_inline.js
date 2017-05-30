$(document).ready(function() {

    // Function to get full calendar events  -----------------v
    function getEvents(id, cb_func) {

        $.ajax({
            type: "POST",
            url: "/get-events/",
            data: JSON.stringify({
                'user_id': id
            }),

            // ------v-------use it as the callback function
            success: cb_func,
            error: function(request, error) {
                console('error');
                // console.log(request, error);
            }
        });
    }




    // Fullcalendar 

    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay,list'
        },


        validRange: function(nowDate) {
            var moment = $('#calendar').fullCalendar('getDate');
            return {
                start: nowDate.format('YYYY-MM-DD')
            };
        },
        navLinks: true,
        selectable: true,
        selectHelper: true,

        select: function(start, end, allDay) {
            // console.log('select is called..')                    
            $('.eventDetailBox').show();
            var star_date = moment(start._d).format('YYYY-MM-DD')
            $('#datetimepicker1').datetimepicker('remove');
            $('#datetimepicker1').datetimepicker({
                startView: 1,
                todayBtn: true,
                startDate: star_date,
            });
            $('#datetimepicker2').datetimepicker('remove');
            $('#datetimepicker2').datetimepicker({
                startView: 1,
                todayBtn: true,
                startDate: star_date,
            });

            $("#dialog").dialog({
                dialogClass: "no-close",
                responsive: true,
                minWidth: 350,
                position: {
                    my: "top",
                    at: "top",
                    of: window
                },
                buttons: {
                    "Submit": function() {
                        var startTime = $('#startTime').val();
                        var endDateTime = $('#endDateTime').val();
                        var title = $('#eventTitle').val();
                        // console.log(moment(endDateTime).isAfter(startTime,'day'))
                        if (startTime == null || startTime == undefined || startTime == "" ||
                            endDateTime == null || endDateTime == undefined || endDateTime == "" ||
                            title == null || title == undefined || title == "") {
                            $.toast({
                                heading: 'Error!',
                                text: 'Please fill all the fields.',
                                position: 'top-center',
                                showHideTransition: 'fade',
                                icon: 'error',
                                textColor: 'white'
                            }); 
                        }
                        else if(moment(endDateTime).isAfter(startTime,'minutes') == false){
                            $.toast({
                                heading: 'Error!',
                                text: 'end date should be bigger than start date.',
                                position: 'top-center',
                                showHideTransition: 'fade',
                                icon: 'error',
                                textColor: 'white'
                            });
                        } 
                        else {
                            $(this).dialog("close");
                            var eventData;
                            eventData = {
                                title: title,
                                start: startTime,
                                end: endDateTime,
                                allDay: false
                            };
                            $.ajax({
                                type: "POST",
                                url: "/create-event/",
                                data: JSON.stringify(eventData),
                                contentType: "application/json",
                                success: function(res) {
                                    eventData['_id'] = res['_id']
                                    $('#calendar').fullCalendar('renderEvent', eventData, true);
                                    $('#startTime').val('');
                                    $('#endDateTime').val('');
                                    $('#eventTitle').val('');

                                }
                            });
                        }
                        $('#calendar').fullCalendar('unselect');
                    },
                    Cancel: function() {
                        $('#calendar').fullCalendar('unselect');
                        $(this).dialog("close");
                    }
                }
            });

        },
        editable: true,
        eventLimit: true, // allow "more" link when too many events
        events: function(start, end, timezone, callback) {

            var id = $('#user_id').val();
            getEvents(id, function(returnValue) {
                callback(returnValue['data'])
            });

        },
        timeFormat: '(h:mm)t',
        eventClick: function(event, jsEvent, view) {
            // console.log(moment('2010-01-20 10:00').isAfter('2010-01-20 11:00', 'day'))
            $('.updateEventBox').show();
            $('#updated_startDateTime').val(event.start._i);
            $('#updated_endDateTime').val(event.end._i);
            $('#updatedTitle').val(event.title);
            $('#updated_datetimepicker1').datetimepicker({
                startView: 1,
                todayBtn: true,
                startDate: moment().format('YYYY-MM-DD'),
            });

            $('#updated_datetimepicker2').datetimepicker({
                startView: 1,
                todayBtn: true,
                startDate: moment().format('YYYY-MM-DD'),
            });
            $("#eventUpdateDialog").dialog({
                dialogClass: "no-close",
                responsive: true,
                minWidth: 350,
                position: {
                    my: "top",
                    at: "top",
                    of: window
                },
                buttons: {
                    "Update": function() {
                        var start = $('#updated_startDateTime').val();
                        var end = $('#updated_endDateTime').val();
                        var title = $('#updatedTitle').val();
                        if (start == null || start == undefined || start == "" ||
                            end == null || end == undefined || end == "" ||
                            title == null || title == undefined || title == "") {
                            $.toast({
                                heading: 'Error!',
                                text: 'Please fill all the fields.',
                                position: 'top-center',
                                showHideTransition: 'fade',
                                icon: 'error',
                                textColor: 'white'
                            }) 
                        } 
                        else if( moment(end).isAfter(start,'minutes') == false ){
                            // alert('end date should be bigger than start date');
                            $.toast({
                                heading: 'Error!',
                                text: 'end date should be bigger than start date.',
                                position: 'top-center',
                                showHideTransition: 'fade',
                                icon: 'error',
                                textColor: 'white'
                            }) 
                        }
                        else {
                            $(this).dialog("close");
                            params = {
                                'start': start,
                                'end': end,
                                'title': title,
                                'event_id': event._id
                            }
                            $.ajax({
                                url: '/update-event/',
                                dataType: 'json',
                                type: "POST",
                                data: JSON.stringify(params),
                                success: function(resp) {                                    
                                         window.location.reload()                                                                                                                                                                                                                                                                                              
                                }
                            });
                        }

                    },
                    "Delete": function() {
                        var delete_flag = confirm("Are you sure you want to delete?");
                        if (delete_flag == true) {
                            $(this).dialog("close");
                            params = {
                                'event_id': event._id
                            }
                            $.ajax({
                                url: '/delete-event/',
                                dataType: 'json',
                                type: "POST",
                                data: JSON.stringify(params),
                                success: function(resp) {

                                    window.location.reload();

                                }

                            });

                        }
                    },
                    "Close": function() {
                        $(this).dialog('close')
                    }
                }
            });
        },
        eventDrop:function( event, delta, revertFunc, jsEvent, ui, view ) { 
        
            if(confirm("Are you sure about to change ?")){
                var start = moment(event.start._d).format('YYYY-MM-DD ')+moment(event.start._i).format('hh:mm')
                var end = moment(event.end._d).format('YYYY-MM-DD ')+moment(event.end._i).format('hh:mm')
                var title = event.title
                var event_id = event._id
                params = { 'start':start , 'end':end, 'title':title, 'event_id':event_id }
                console.log('params',params)
                $.ajax({
                    url: '/update-event/',
                    dataType: 'json',
                    type: "POST",
                    data: JSON.stringify(params),
                    success: function(resp) { 
                        window.location.reload();                                                                                                                                                                                                                           
                    }
                });
            }
            else{
                revertFunc();
            }
         }   
    });

});