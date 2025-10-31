// // Actions:

// const closeButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>remove</title>
// <path d="M27.314 6.019l-1.333-1.333-9.98 9.981-9.981-9.981-1.333 1.333 9.981 9.981-9.981 9.98 1.333 1.333 9.981-9.98 9.98 9.98 1.333-1.333-9.98-9.98 9.98-9.981z"></path>
// </svg>
// `;
// const menuButton = `<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
// <title>ellipsis-horizontal</title>
// <path d="M16 7.843c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 1.98c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 19.908c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 14.046c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// <path d="M16 31.974c-2.156 0-3.908-1.753-3.908-3.908s1.753-3.908 3.908-3.908c2.156 0 3.908 1.753 3.908 3.908s-1.753 3.908-3.908 3.908zM16 26.111c-1.077 0-1.954 0.877-1.954 1.954s0.877 1.954 1.954 1.954c1.077 0 1.954-0.877 1.954-1.954s-0.877-1.954-1.954-1.954z"></path>
// </svg>
// `;

// const actionButtons = document.querySelectorAll('.action-button');

// if (actionButtons) {
//   actionButtons.forEach(button => {
//     button.addEventListener('click', () => {
//       const buttonId = button.dataset.id;
//       let popup = document.querySelector(`.popup-${buttonId}`);
//       console.log(popup);
//       if (popup) {
//         button.innerHTML = menuButton;
//         return popup.remove();
//       }

//       const deleteUrl = button.dataset.deleteUrl;
//       const editUrl = button.dataset.editUrl;
//       button.innerHTML = closeButton;

//       popup = document.createElement('div');
//       popup.classList.add('popup');
//       popup.classList.add(`popup-${buttonId}`);
//       popup.innerHTML = `<a href="${editUrl}">Edit</a>
//       <form action="${deleteUrl}" method="delete">
//         <button type="submit">Delete</button>
//       </form>`;
//       button.insertAdjacentElement('afterend', popup);
//     });
//   });
// }

// Menu functionality
// Simple and clean JavaScript
const dropdownMenu = document.querySelector(".dropdown-menu");
const dropdownButton = document.querySelector(".dropdown-button");

if (dropdownButton) {
  dropdownButton.addEventListener("click", () => {
    dropdownMenu.classList.toggle("show");
  });
}

// Upload Image
const photoInput = document.querySelector("#avatar");
const photoPreview = document.querySelector("#preview-avatar");
if (photoInput) {
  photoInput.onchange = () => {
    const [file] = photoInput.files;
    if (file) {
      photoPreview.src = URL.createObjectURL(file);
    }
  };
}

// Scroll to Bottom
const conversationThread = document.querySelector(".room__box");
if (conversationThread) conversationThread.scrollTop = conversationThread.scrollHeight;

// Code Snippet Functionality
function initializeCodeSnippetFeatures() {
    const codeSnippetToggle = document.getElementById('is_code_snippet');
    const codeControls = document.getElementById('codeControls');
    const messageTextarea = document.getElementById('messageTextarea');
    const languageSelect = document.getElementById('language');

    if (codeSnippetToggle && codeControls && messageTextarea) {
        // Make code controls always visible
        codeControls.style.display = 'block';

        // Toggle code snippet mode
        codeSnippetToggle.addEventListener('change', function() {
            if (this.checked) {
                // Code mode ON
                codeControls.style.backgroundColor = 'var(--color-dark-light)';
                codeControls.style.border = '2px solid var(--color-main)';
                messageTextarea.placeholder = 'Paste your code here...';
                messageTextarea.rows = 8;
                messageTextarea.style.fontFamily = 'Monaco, "Courier New", monospace';
                messageTextarea.style.fontSize = '13px';
            } else {
                // Code mode OFF
                codeControls.style.backgroundColor = 'var(--color-dark-medium)';
                codeControls.style.border = '1px solid var(--color-dark-light)';
                messageTextarea.placeholder = 'Write your message here...';
                messageTextarea.rows = 3;
                messageTextarea.style.fontFamily = 'inherit';
                messageTextarea.style.fontSize = '14px';
            }
        });

        // Tab support for code indentation
        messageTextarea.addEventListener('keydown', function(e) {
            if (e.key === 'Tab' && codeSnippetToggle.checked) {
                e.preventDefault();
                const start = this.selectionStart;
                const end = this.selectionEnd;
                
                // Insert 4 spaces
                this.value = this.value.substring(0, start) + '    ' + this.value.substring(end);
                
                // Move cursor
                this.selectionStart = this.selectionEnd = start + 4;
            }
        });
    }
}

// Copy code functionality
function copyCode(button) {
    const codeBlock = button.closest('.code-snippet').querySelector('code');
    const textArea = document.createElement('textarea');
    textArea.value = codeBlock.textContent;
    document.body.appendChild(textArea);
    textArea.select();
    document.execCommand('copy');
    document.body.removeChild(textArea);
    
    // Visual feedback
    const originalText = button.innerHTML;
    button.innerHTML = '✓ Copied!';
    button.style.background = 'var(--color-success)';
    button.style.borderColor = 'var(--color-success)';
    button.style.color = 'var(--color-dark)';
    
    setTimeout(() => {
        button.innerHTML = originalText;
        button.style.background = 'transparent';
        button.style.borderColor = 'var(--color-main)';
        button.style.color = 'var(--color-main)';
    }, 2000);
}

// Initialize when page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeCodeSnippetFeatures();
});