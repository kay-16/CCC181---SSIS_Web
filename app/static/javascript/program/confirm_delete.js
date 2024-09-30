function confirmDeleteProgram(courseCode) {
    showYoyoPopup({
        text: `Warning! Are you sure you want to delete ${courseCode}?`,
        subtext: `Note: THIS ACTION CANNOT BE UNDONE. Once deleted, all students enrolled in ${courseCode} will be unenrolled.`,
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
            form.action = `/programs/delete/${courseCode}`;  // Ensure the action matches the route

            // Create hidden input for CSRF token
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrf_token';
            csrfInput.value = csrfToken;  // Set the CSRF token
            form.appendChild(csrfInput);

            document.body.appendChild(form);
            form.submit();  // Submit the form to delete the program
        },
        cancelFunction: () => {
            console.log("Deletion cancelled");
        },
        closeFunction: () => {
            console.log("Popup closed");
        },
    });
}
