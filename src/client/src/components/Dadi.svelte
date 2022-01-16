<script>
  import { range } from '../utils.js';
  import { fade } from 'svelte/transition';
  let facce = {
    nero: [0, 1, 1, 1, 2, 2],
    blu: [1, 1, 2, 2, 2, 3],
    arancio: [1, 2, 2, 3, 3, 4]
  };

  let dadi = [
    { colore: 'nero', valori: [] },
    { colore: 'blu', valori: [] },
    { colore: 'arancio', valori: [] }
  ];

  $: total = dadi.reduce((acc, dado) => acc + dado.valori.reduce((acc, v) => acc + v, 0), 0);

  function aggiungi(dado) {
    dado.valori.push(0);
    dadi = dadi;
  }
  function rimuovi(dado) {
    dado.valori.pop(0);
    dadi = dadi;
  }
  function lancia() {
    dadi = dadi.map(dado => {
      return {
        ...dado,
        valori: dado.valori.map(i => facce[dado.colore][Math.floor(Math.random() * 6)])
      };
    });
  }
  function resetta() {
    dadi = dadi.map(dado => {
      return { ...dado, valori: [] };
    });
  }
</script>

<div class="scelta-dadi">
  {#each dadi as dado}
    <div class={dado.colore}>
      <span class="sign" on:click={() => rimuovi(dado)}>−</span>
      <span class="colore">{dado.valori.length}</span>
      <span class="sign" on:click={() => aggiungi(dado)}>+</span>
    </div>
  {/each}
</div>
<div class="flex">
  <button class="ds-btn" on:click={lancia}>LANCIA</button>
  <button class="ds-btn" on:click={resetta}>RESETTA</button>
  <div class="total">{total}</div>
</div>
<div class="lista-dadi">
  {#each dadi as dado}
    <div class="dadi-{dado.colore}">
      {#each dado.valori as valore}
        <span class="dado {dado.colore}" on:click={() => rimuovi(dado)} transition:fade>
          <img src="images/dadi/{valore}.png" alt="dado-{dado.colore}" />
        </span>
      {/each}
    </div>
  {/each}
</div>
<br />

<style>
  .scelta-dadi {
    display: flex;
    width: inherit;
    padding: 20px;
    justify-content: space-around;
  }

  .sign {
    user-select: none;
    cursor: pointer;
    display: inline-block;
    width: 25px;
    height: 25px;
    background: #ffffff;
    color: #404040;
    border-radius: 50%;
    text-align: center;
    font-weight: bold;
    line-height: 26px;
    font-size: 26px;
  }

  .sign:hover {
    background: #cecac8;
  }
  .sign:active {
    background: #a1a1a1;
  }

  .colore {
    display: inline-block;
    width: 50px;
    height: 50px;
    background: #ccc6bf;
    color: #404040;
    border-radius: 50%;
    margin: 5px;
    border: 1px solid white;
    color: white;
    text-align: center;
    font-size: 27px;
    line-height: 50px;
  }

  .nero .colore {
    background: #716d6d;
    box-shadow: inset #000000 0 0 20px 7px;
  }
  .blu .colore {
    background: #72aaff;
    box-shadow: inset #245eb6 0 0 20px 10px;
  }
  .arancio .colore {
    background: #ffcb86;
    box-shadow: inset #b86800 0 0 20px 10px;
  }

  .lista-dadi {
    height: fit-content;
    padding: 20px;
  }

  .lista-dadi .dado {
    display: inline-block;
    width: 70px;
    height: 70px;
    border-radius: 10px;
    margin: 0 16px 16px 0;
    box-shadow: 1px 5px 9px 2px #000000bf;
    transition: all 0.5s linear;
  }
  .lista-dadi .dado:last-child {
    margin: 0 13px 16px 0;
  }

  .lista-dadi .dado img {
    width: inherit;
  }

  .lista-dadi .dado.nero {
    background: linear-gradient(45deg, black, #464646);
  }
  .lista-dadi .dado.blu {
    background: linear-gradient(45deg, rgb(24, 76, 154), rgb(63, 139, 255));
  }
  .lista-dadi .dado.arancio {
    background: linear-gradient(45deg, rgb(128, 79, 16), rgb(247, 139, 0));
  }

  .lista-dadi span {
    margin: 0;
  }

  .total {
    font-size: 40px;
    border: white solid 2px;
    border-radius: 50%;
    width: 55px;
    height: 55px;
    line-height: 57px;
    text-align: center;
    color: white;
  }

  .flex {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }
  * {
    user-select: none;
  }
</style>
