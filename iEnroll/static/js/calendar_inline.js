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

        // navLinkDayClick: function(weekStart, jsEvent) {
        //     $('#calendar').fullCalendar('changeView', 'agendaDay');
        // },
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
            var startDate = start.format('YYYY-MM-DD').toString();             
            $('.eventDetailBox').show();
            $('#datetimepicker1').datetimepicker({
                startView:1,
                startDate:startDate
                });

            $('#datetimepicker2').datetimepicker({
                startView:1,
                startDate:startDate
            });
            $('#datetimepicker1').datetimepicker('setStartDate', startDate);
            $('#datetimepicker2').datetimepicker('setStartDate', startDate);
            $('#datetimepicker1').datetimepicker('update');
            $('#datetimepicker2').datetimepicker('update');
            $( "#dialog" ).dialog({    
                dialogClass: "no-close",
                responsive: true,
                minWidth:350,
                position:{ my: "top", at: "top", of: window },
                buttons: {
                "Submit": function() {
                        var startTime = $('#startTime').val();
                        var endDateTime = $('#endDateTime').val();
                        var title = $('#eventTitle').val();
                        if(startTime == null || startTime == undefined || startTime == "" || 
                            endDateTime ==  null || endDateTime == undefined || endDateTime == "" ||
                            title == null || title == undefined || title == ""){
                            alert( 'fill all details');
                        }
                        else{
                            $( this ).dialog( "close" );
                            var eventData;
                            eventData = {
                                title: title,
                                start: startTime,
                                end: endDateTime,
                                allDay:false
                            };
                            $.ajax({
                                type: "POST",
                                url: "/create-event/",
                                data: JSON.stringify(eventData),
                                contentType: "application/json",
                                success: function(res) {
                                    console.log('response', res['_id'])
                                    eventData['_id'] = res['_id']
                                    $('#calendar').fullCalendar('renderEvent', eventData, true);

                                }
                            });
                        }
                    },
                    Cancel: function() {
                      $( this ).dialog( "close" );
                    }
                }
            });           
            $('#calendar').fullCalendar('unselect');
        },
        editable:false,
        eventLimit: true, // allow "more" link when too many events
        events: function(start, end, timezone, callback) {

           
            var id = $('#user_id').val();
            
            getEvents(id, function(returnValue) {
                callback(returnValue['data'])
            });

        },
        timeFormat: '(h:mm)t',
         // can click day/week names to navigate views

        // eventDrop: function(event, delta, revertFunc) {
        //     if (confirm("Are you sure about this change?")) {
        //         console.log(event);
        //         params = {
        //             'title': event.title,
        //             'start': event.start.format('YYYY-MM-DD'),
        //             'end': event.end.format('YYYY-MM-DD'),
        //             'id': event._id
        //         }
        //         console.log('params', params)
        //         $.ajax({
        //             url: '/update-event/',
        //             dataType: 'json',
        //             type: "POST",
        //             data: JSON.stringify(params),
        //             success: function(response) {
        //                 console.log('response', response)

        //             }

        //         })

        //     } else {
        //         revertFunc();
        //     }

        // },
        
        


    });
    
});