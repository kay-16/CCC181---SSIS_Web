function confirmDelete(studentId) {
    showYoyoPopup({
        text: 'Are you sure to delete this student?',
        subtext: 'THIS ACTION CANNOT BE UNDONE.',
        type: 'danger',
        isStatic: true,
        hasConfirmation: true,
        hasCancellation: true,
        confirmLabel: 'Yes, Proceed',
        cancelLabel: 'Cancel',
        closeLabel: 'Close',
        formId: '',  // if needed for form ID
        confirmFunction: () => {
            // If confirmed, submit the deletion form
            const form = document.createElement('form');
            form.method = 'POST';
            form.action = `/delete/${studentId}`;  // Ensure the action matches the route
            document.body.appendChild(form);
            form.submit();  // Submit the form to delete the student
        },
        cancelFunction: () => {
            // Handles cancellation
            console.log("Deletion cancelled");
        },
        closeFunction: () => {
            console.log("Popup closed");
        },
    });
}
