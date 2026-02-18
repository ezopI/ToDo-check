document.querySelectorAll(".todo-check").forEach((checkbox) => {
    checkbox.addEventListener("change", async (e) => {
        const id = e.target.dataset.id;

        // Enviar POST para backend
        const res = await fetch(`/toggle/${id}`, { method: "POST" });
        const data = await res.json();
        // Encontrar o titulos para o toDo
        const title = document.querySelector(`[data-title-id="${id}"]`);
        // If done == 1 -> adiciona a classe "done", else remove
        if (data.completed === 1) {
            title.classList.add("done");
        } else {
            title.classList.remove("done");
        }
    });
});