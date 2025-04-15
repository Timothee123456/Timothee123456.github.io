const containers = document.querySelectorAll('.tooltip_container, .tooltip_container_left');

containers.forEach(container => {
    const tooltip = container.querySelector('.tooltip');
    let timeoutId;

    container.addEventListener('mouseover', (e) => {
        timeoutId = setTimeout(() => {
            tooltip.style.opacity = 1;
            let x = e.clientX;
            let y = e.clientY + 10;

            // Check if it's the left-side container
            if (container.classList.contains('tooltip_container_left')) {
                x = e.clientX - tooltip.offsetWidth - 10; // Position to the left
            } else {
                x = e.clientX + 10; // Position to the right
            }

            tooltip.style.left = x + 'px';
            tooltip.style.top = y + 'px';
        }, 700); // 700 milliseconds delay
    });

    container.addEventListener('mouseout', () => {
        clearTimeout(timeoutId);
        tooltip.style.opacity = 0;
    });
});
