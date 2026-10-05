// ---------- DADOS ----------

// Recupera os álbuns salvos (ou começa com lista vazia)
let salvos = [];
try {
  salvos = JSON.parse(localStorage.getItem("albunsSalvos")) || [];
} catch (e) {
  salvos = [];
}

// ---------- ELEMENTOS DO AVATAR / PAINEL ----------
// Ficam no topo para existirem antes de qualquer função que use eles
const avatarBtn = document.querySelector(".avatar-btn");
const painel = document.querySelector(".painel-salvos");
const lista = document.querySelector("#lista-salvos");

// Monta a lista de álbuns salvos dentro do painel
function atualizarLista() {
  lista.innerHTML = "";

  if (salvos.length === 0) {
    lista.innerHTML = "<li>Nenhum álbum salvo ainda</li>";
    return;
  }

  salvos.forEach((nome) => {
    const li = document.createElement("li");
    li.textContent = nome;
    lista.appendChild(li);
  });
}

// ---------- BOTÕES SALVAR ----------

const botoes = document.querySelectorAll(".btn-salvar");

botoes.forEach((botao) => {
  // Usa o título (h2) do card como identificador do álbum
  const card = botao.closest(".card");
  const nome = card.querySelector("h2").textContent.trim();

  // Ao carregar, marca como salvo quem já estava salvo
  if (salvos.includes(nome)) {
    botao.classList.add("salvo");
  }
  botao.setAttribute("aria-pressed", salvos.includes(nome));

  // Ao clicar, salva ou remove
  botao.addEventListener("click", () => {
    const posicao = salvos.indexOf(nome);

    if (posicao === -1) {
      salvos.push(nome);
    } else {
      salvos.splice(posicao, 1);
    }

    botao.classList.toggle("salvo");
    botao.setAttribute("aria-pressed", botao.classList.contains("salvo"));
    localStorage.setItem("albunsSalvos", JSON.stringify(salvos));
    atualizarLista(); // mantém o painel atualizado
  });
});

// ---------- AVATAR: ABRE / FECHA O PAINEL ----------

avatarBtn.addEventListener("click", () => {
  const estavaAberto = !painel.hidden;
  painel.hidden = estavaAberto; // abre ou fecha
  avatarBtn.setAttribute("aria-expanded", !estavaAberto);
  atualizarLista();
});

// Fecha com a tecla Esc
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    painel.hidden = true;
    avatarBtn.setAttribute("aria-expanded", "false");
  }
});

// ---------- LUZ QUE SEGUE O MOUSE ----------

document.addEventListener("mousemove", (e) => {
  document.body.style.setProperty("--x", e.clientX + "px");
  document.body.style.setProperty("--y", e.clientY + "px");
});

// ---------- EFEITO 3D NOS CARDS ----------

document.querySelectorAll(".card").forEach((card) => {
  card.addEventListener("mousemove", (e) => {
    const r = card.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;   // -0.5 a 0.5
    const y = (e.clientY - r.top) / r.height - 0.5;

    card.style.setProperty("--ry", x * 12 + "deg");
    card.style.setProperty("--rx", y * -12 + "deg");
  });

  card.addEventListener("mouseleave", () => {
    card.style.setProperty("--rx", "0deg");
    card.style.setProperty("--ry", "0deg");
  });
});

// Monta a lista uma vez ao carregar (agora tudo já existe)
atualizarLista();