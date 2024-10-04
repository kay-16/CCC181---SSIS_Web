function confirmDeleteCollege(collegeCode) {
    showYoyoPopup({
        text: `Warning! Are you sure you want to delete ${collegeCode}?`,
        subtext: `Note: THIS ACTION CANNOT BE UNDONE. Once deleted, all programs under ${collegeCode} will be deleted and students will be marked 'Unenrolled'.`,
        type: 'danger', 
        isStatic: true,
        hasConfirmation: true,
        hasCancellation: true,
        confirmLabel: 'Yes, Proceed',
        cancelLabel: 'Cancel',
        closeLabel: 'Close',
        confirmFunction: () => {
            // If confirmed, submit the deletion form
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/college/delete/${collegeCode}`;  // Ensure the action matches the route

            // Create hidden input for CSRF token
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrf_token';
            csrfInput.value = csrfToken;  // Set the CSRF token
            form.appendChild(csrfInput);

            document.body.appendChild(form);
            form.submit();  // Submit the form to delete the college
        },
        cancelFunction: () => {
            console.log("Deletion cancelled");
        },
        closeFunction: () => {
            console.log("Popup closed");
        },
    });
}
