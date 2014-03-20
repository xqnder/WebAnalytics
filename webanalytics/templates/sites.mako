<html>

<head>
  <title>Site statistics</title>
</head>

<table>

<thead class="person">
    <tr>
        <th>ID</th>
        <th>Address</th>
        <th>Visits</th>
        <th>Total visit time</th>
        <th>Child visits</th>
        <th>Total child visit time</th>
    </tr>
</thead>

<tbody class="sites">
    % for site in sites:
        <tr>
            <td>${ site.id }</td>
            <td>${ site.address }</td>
            <td>${ site.visits }</td>
            <td>${ site.total_visit_time }</td>
            <td>${ site.child_visits }</td>
            <td>${ site.total_child_visit_time }</td>
        </tr>
    % endfor
</tbody>

</table>

</html>