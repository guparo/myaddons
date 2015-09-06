<html>
<head>
    <style type="text/css">
        ${css}
    </style>
</head>
<body>
    % for session in objects:
    <h1>${session.name|entity}</h1>
    <h2>Course: ${session.course_id.name|entity}</h2>
    ${session.course_id.description|entity}
    <h2>Schedule</h2>
    % if session.start_date:
    Starts on ${formatLang(session.start_date, date=True)}.
    % endif
    % if session.duration:
    Lasts ${formatLang(session.duration, digits=1)} days.
    % endif
    % if session.instructor_id:
    Given by ${session.instructor_id.name|entity}.
    % endif
    <h2>Attendees</h2>
    <ul>
        % for attendee in session.attendee_ids:
        <li>${attendee.partner_id.name|entity}</li>
        % endfor
    </ul>
    % endfor
</body>
</html>
