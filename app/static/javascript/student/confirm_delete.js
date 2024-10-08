function confirmDeleteStudent(studentId) {
    showYoyoPopup({
        text: `Warning! Are you sure you want to delete student with ID number ${studentId}?`,
        subtext: 'This action cannot be undone.',
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
            form.action = `/delete/${studentId}`;  // Ensure the action matches the route

            // Create hidden input for CSRF token
            const csrfInput = document.createElement('input');
            csrfInput.type = 'hidden';
            csrfInput.name = 'csrf_token';
            csrfInput.value = csrfToken;  // Set the CSRF token
            form.appendChild(csrfInput);

            document.body.appendChild(form);
            form.submit();  // Submit the form to delete the student
        },
        cancelFunction: () => {
            console.log("Deletion cancelled");
        },
        closeFunction: () => {
            console.log("Popup closed");
        },
    });
}
