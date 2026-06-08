const STORAGE_KEY = "chinese-todo-items";

const todoForm = document.querySelector("#todo-form");
const todoInput = document.querySelector("#todo-input");
const todoList = document.querySelector("#todo-list");
const todoCount = document.querySelector("#todo-count");
const emptyState = document.querySelector("#empty-state");
const todoTemplate = document.querySelector("#todo-template");
const todayDate = document.querySelector("#today-date");

let todos = loadTodos();

function loadTodos() {
  try {
    const savedTodos = JSON.parse(localStorage.getItem(STORAGE_KEY));

    if (!Array.isArray(savedTodos)) {
      return [];
    }

    return savedTodos.filter((todo) => (
      todo
      && typeof todo.id === "string"
      && typeof todo.text === "string"
      && typeof todo.completed === "boolean"
    ));
  } catch (error) {
    console.warn("无法读取已保存的待办事项：", error);
    return [];
  }
}

function saveTodos() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(todos));
  } catch (error) {
    console.warn("无法保存待办事项：", error);
  }
}

function createTodoId() {
  if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
    return crypto.randomUUID();
  }

  return `${Date.now()}-${Math.random().toString(16).slice(2)}`;
}

function updateSummary() {
  const remainingCount = todos.filter((todo) => !todo.completed).length;
  const completedCount = todos.length - remainingCount;

  if (todos.length === 0) {
    todoCount.textContent = "还没有待办事项";
  } else if (remainingCount === 0) {
    todoCount.textContent = `全部完成，共 ${completedCount} 项`;
  } else {
    todoCount.textContent = `${remainingCount} 项待完成 · ${completedCount} 项已完成`;
  }

  emptyState.hidden = todos.length > 0;
}

function renderTodos() {
  todoList.replaceChildren();

  todos.forEach((todo) => {
    const todoItem = todoTemplate.content.firstElementChild.cloneNode(true);
    const toggleButton = todoItem.querySelector(".toggle-button");
    const deleteButton = todoItem.querySelector(".delete-button");
    const todoText = todoItem.querySelector(".todo-text");

    todoItem.dataset.id = todo.id;
    todoItem.classList.toggle("completed", todo.completed);
    todoText.textContent = todo.text;
    toggleButton.setAttribute("aria-label", todo.completed ? "取消完成" : "标记为已完成");
    toggleButton.setAttribute("aria-pressed", String(todo.completed));
    deleteButton.setAttribute("aria-label", `删除待办事项：${todo.text}`);

    todoList.append(todoItem);
  });

  updateSummary();
}

function addTodo(text) {
  todos.unshift({
    id: createTodoId(),
    text,
    completed: false,
  });
  saveTodos();
  renderTodos();
}

function toggleTodo(id) {
  todos = todos.map((todo) => (
    todo.id === id ? { ...todo, completed: !todo.completed } : todo
  ));
  saveTodos();
  renderTodos();
}

function deleteTodo(id) {
  todos = todos.filter((todo) => todo.id !== id);
  saveTodos();
  renderTodos();
}

function displayCurrentDate() {
  const formattedDate = new Intl.DateTimeFormat("zh-CN", {
    month: "long",
    day: "numeric",
    weekday: "long",
  }).format(new Date());

  todayDate.textContent = formattedDate;
}

todoForm.addEventListener("submit", (event) => {
  event.preventDefault();
  const todoText = todoInput.value.trim();

  if (!todoText) {
    todoInput.focus();
    return;
  }

  addTodo(todoText);
  todoForm.reset();
  todoInput.focus();
});

todoList.addEventListener("click", (event) => {
  const todoItem = event.target.closest(".todo-item");

  if (!todoItem) {
    return;
  }

  if (event.target.closest(".toggle-button")) {
    toggleTodo(todoItem.dataset.id);
  }

  if (event.target.closest(".delete-button")) {
    deleteTodo(todoItem.dataset.id);
  }
});

displayCurrentDate();
renderTodos();
