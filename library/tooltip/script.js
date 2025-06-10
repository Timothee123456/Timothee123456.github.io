const containers = document.querySelectorAll('.tooltip_container');

    containers.forEach(container => {
        const tooltip = container.querySelector('.tooltip');
        let timeoutId;

        container.addEventListener('mousemove', (e) => {
            clearTimeout(timeoutId);
            timeoutId = setTimeout(() => {
                tooltip.classList.add('visible');
                updateTooltipPosition(e, tooltip);
            }, 700); // 700 milliseconds delay
        });

        container.addEventListener('mouseout', () => {
            clearTimeout(timeoutId);
            tooltip.classList.remove('visible');
        });

        function updateTooltipPosition(e, tooltip) {
            let x = e.clientX;
            let y = e.clientY + 10;  // Offset from the mouse

            // Check if the tooltip will overflow the viewport
            const tooltipRect = tooltip.getBoundingClientRect();

            if (x + tooltipRect.width > window.innerWidth) {
                x = window.innerWidth - tooltipRect.width - 10;  // Keep it within the right boundary
            }

            if (x < 0) {
                x = 10;  // Keep it within the left boundary
            }

            // Apply the calculated positions
            tooltip.style.left = x + 'px';
            tooltip.style.top = y + 'px';
        }
    });
