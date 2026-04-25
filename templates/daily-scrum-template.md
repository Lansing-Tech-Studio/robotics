---
layout: note
title: "Daily Scrum"
---

<style>
  /* Print-first scrum form */
  .scrum-form { font-family: "Segoe UI", Arial, sans-serif; }
  .scrum-form .field-row { margin-bottom: 0.5em; }
  .scrum-form .blank {
    display: inline-block;
    border-bottom: 1px solid #000;
    min-width: 10em;
  }
  .scrum-form .blank-wide {
    display: inline-block;
    border-bottom: 1px solid #000;
    min-width: 20em;
  }
  .scrum-form table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1em;
  }
  .scrum-form th {
    text-align: left;
    border-bottom: 2px solid #000;
    padding: 0.2em 0.5em;
    font-size: 0.95em;
  }
  .scrum-form td {
    border-bottom: 1px solid #ccc;
    padding: 0.6em 0.5em;
    height: 2em;
    vertical-align: top;
  }
  .scrum-form h2 {
    margin-top: 0.8em;
    margin-bottom: 0.3em;
    font-size: 1.1em;
  }
  .scrum-form .attendee-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 0.4em 2em;
    margin-bottom: 1em;
  }
  .scrum-form .attendee-line {
    display: flex;
    align-items: center;
    gap: 0.5em;
  }
  .scrum-form .attendee-line .bullet::before {
    content: "›";
    font-size: 1.3em;
    font-weight: bold;
    line-height: 1;
  }
  .scrum-form .attendee-line .bullet {
    flex-shrink: 0;
  }
  .scrum-form .attendee-line .blank {
    flex-grow: 1;
  }
  .scrum-form .notes-area {
    border: 1px solid #ccc;
    min-height: 6em;
    padding: 0.5em;
  }
  @media print {
    .scrum-form { font-size: 11pt; }
    .scrum-form td {
      border-bottom: 1px solid #fff;
      border-top: 1px solid #fff;
    }
    .scrum-form th {
      border-top: 1px solid #fff;
    }
  }
</style>

<div class="scrum-form" markdown="0">

<div class="field-row">
  <strong>Team:</strong> <span class="blank-wide">&nbsp;</span>
  &emsp;
  <strong>Date:</strong> <span class="blank">&nbsp;</span>
</div>

<h2>Attendees</h2>
<div class="attendee-grid">
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
  <div class="attendee-line"><span class="bullet"></span><span class="blank">&nbsp;</span></div>
</div>

<h2>What did we accomplish since last meeting?</h2>
<table>
  <tr><th>Who</th><th>What they did</th></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
</table>

<h2>What are we working on today?</h2>
<table>
  <tr><th>Task</th><th>Goal/Criteria</th></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
</table>

<h2>Blockers</h2>
<table>
  <tr><th width="40%">Blocker</th><th width="30%">Assignee</th><th width="30%">Help needed from</th></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
  <tr><td></td><td></td><td></td></tr>
</table>

<span class="page-break-after">&nbsp;</span>

<h2>What were the insights for today? What changes or adaptations did you make?</h2>
<table>
  <tr><th>Notes</th></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
</table>

<h2>What do you hope to accomplish next meeting?</h2>
<table>
  <tr><th>Notes</th></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
  <tr><td></td></tr>
</table>

<h2>Is there anything that needs to be done before next meeting?</h2>
<table>
  <tr><th>Who</th><th>What they'll do</th></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
  <tr><td></td><td></td></tr>
</table>

</div>
