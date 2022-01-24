<script>
  import { createEventDispatcher } from 'svelte';
  import { isEmpty } from '../utils.js';
  export let card = {};
  export let id = '';
  export let type = '';

  const dispatch = createEventDispatcher();
  function openAddCardModal() {
    dispatch('add', { id, type });
  }
  function openEditCardModal() {
    dispatch('edit', { id, type, ...card });
  }

  // TODO gestire il muovi con il numerino dentro
</script>

<div class="blocco {id}">
  {#if !isEmpty(card)}
    <div class="carta">
      <div class="cerchio portata">
        <img src="images/portata.png" width="20" height="20" alt="portata" />
        {card.portata}
      </div>
      <div class="nome">{card.nome}</div>
      <div class="cerchio impugnatura">
        <img src="images/{card.impugnatura}_mano.png" width="45" height="45" alt="impugnatura" />
      </div>
      <div class="livelli">
        <div class="forza">
          <img src="images/simbolo-forza.png" alt="forza" />
          {card.forza}
        </div>
        <div class="destrezza">
          <img src="images/simbolo-destrezza.png" alt="destrezza" />
          {card.destrezza}
        </div>
        <div class="intelligenza">
          <img src="images/simbolo-intelligenza.png" alt="intelligenza" />
          {card.intelligenza}
        </div>
        <div class="fede">
          <img src="images/simbolo-fede.png" alt="fede" />
          {card.fede}
        </div>
      </div>
      <div class="immagine">
        <img
          src="https://darksouls3.wiki.fextralife.com/file/Dark-Souls-3/{card.immagine}.png"
          alt="immagine"
          height="80" />
      </div>
      <div class="attacchi">
        <table>
          {#each card.attacchi as attacco}
            <tr>
              <td>[{attacco.costo}]</td>
              <td class="attacco">
                {#each attacco.icone as icona}
                  <div class="icona">
                    <img src="images/{icona.immagine}.png" alt={icona.immagine} />
                    {#if icona.valore}
                      <span class="valore">{icona.valore}</span>
                    {/if}
                  </div>
                {/each}
              </td>
            </tr>
          {/each}

        </table>
      </div>
      <div class="difesa scudo">
        <img src="images/scudo.png" alt="scudo" />
        {#if card.scudo.colore}
          <img class="dado" src="images/dado {card.scudo.colore}.png" alt="dado scudo" />
        {/if}
        <span class="valore {card.scudo.colore ? '' : 'no-dado'}">{card.scudo.valore}</span>
      </div>
      <div class="difesa contrasto">
        <img src="images/contrasto.png" alt="contrasto" />
        {#if card.contrasto.colore}
          <img class="dado" src="images/dado {card.contrasto.colore}.png" alt="dado contrasto" />
        {/if}
        <span class="valore {card.contrasto.colore ? '' : 'no-dado'}">{card.contrasto.valore}</span>
      </div>
      <div class="cerchio schivata" alt="schivata">
        <img src="images/schivata.png" alt="dado schivata" />
        <span class="valore">{card.schivata}</span>
      </div>
      <div class="cerchio potenziamenti" alt="potenziamenti">
        <img src="images/potenziamenti.png" alt="dado potenziamenti" />
        <span class="valore">{card.potenziamenti}</span>
      </div>
      <div class="small-btn-container">
        <div class="small-btn edit" on:click={openEditCardModal}>M</div>
        <div class="small-btn delete" on:click={() => (card = {})}>×</div>
      </div>
    </div>
  {:else}
    <div class="small-btn-container">
      <div class="small-btn add" on:click={openAddCardModal}>+</div>
    </div>
    <img src="images/{type}.png" alt={type} class="bg-icon" />
  {/if}
</div>

<style>
  .bg-icon {
    width: 100px;
    height: 100px;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .blocco {
    width: -webkit-fill-available;
    height: -webkit-fill-available;
  }

  .cerchio {
    width: 40px;
    height: 40px;
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
    border-radius: 50%;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: space-around;
    line-height: 1;
    color: black;
  }

  .cerchio img {
    max-width: 98%;
  }

  .carta {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: 1fr 1fr 1fr 2fr 1fr;
    height: 100%;
    grid-template-areas:
      'portata  nome      nome     impugnatura'
      'livelli  immagine  immagine immagine'
      'livelli  immagine  immagine immagine'
      'attacchi attacchi  attacchi attacchi'
      'scudo    contrasto schivata potenziamenti';
    text-align: center;
    background: linear-gradient(45deg, #040b11, #2c373d);
    border-radius: 7px;
    padding: 5px;
    transition: transform 0.2s ease-out;
    position: relative;
    z-index: 2;
    user-select: none;
    -webkit-user-select: none;
    font-size: 13px;
    font-weight: bold;
  }

  .carta > div {
    margin: 3px;
  }

  .portata {
    grid-area: portata;
  }
  .nome {
    grid-area: nome;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
    font-weight: normal;
  }
  .impugnatura {
    grid-area: impugnatura;
  }
  .livelli {
    grid-area: livelli;
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
    padding: 1px 2px 0 3px;
    padding-bottom: 2px;
    display: flex;
    flex-direction: column;
    justify-content: space-around;
  }
  .livelli > div {
    display: flex;
    align-items: center;
    justify-content: space-between;
    border-bottom: 1px #65564159 dashed;
  }
  .livelli > div:last-child {
    border-bottom: none;
  }

  .livelli img {
    width: 46%;
    padding-right: 3px;
    padding-bottom: 3px;
    border-right: 1px #65564159 dashed;
  }
  .immagine {
    grid-area: immagine;
  }
  .attacchi {
    grid-area: attacchi;
    background: #efe4d8;
    box-shadow: inset 0 0 10px 9px #afa18f;
    border: 2px solid #655641;
  }
  .attacchi table {
    width: 100%;
    height: 100%;
    font-size: 17px;
  }
  .attacchi table td:first-child {
    width: 32px;
    border-right: 1px dashed #65564159;
  }
  .attacchi table tr:not(:last-child) td {
    border-bottom: 1px dashed #65564159;
  }

  .attacchi .attacco {
    display: flex;
    align-items: center;
    height: 100%;
  }
  .attacchi .icona {
    position: relative;
    width: 32px;
  }
  .attacchi .icona img {
    width: 80%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .attacchi .icona .valore {
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }

  .scudo {
    grid-area: scudo;
    position: relative;
  }

  .difesa {
    width: 40px;
    height: 40px;
  }

  .difesa > img {
    width: 100%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .difesa .dado {
    width: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
  .difesa .valore {
    position: absolute;
    z-index: 2;
    font-size: 18px;
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .no-dado.valore {
    color: black;
  }

  .contrasto {
    grid-area: contrasto;
    position: relative;
  }
  .contrasto > img {
    width: 100%;
  }
  .contrasto .dado {
    width: 70%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 2;
  }
  .schivata {
    grid-area: schivata;
    position: relative;
  }
  .schivata img {
    width: 77%;
    position: absolute;
    bottom: 0;
    left: 50%;
    transform: translate(-50%, 0);
  }
  .schivata .valore {
    color: black;
    position: absolute;
    top: 5px;
    right: 6px;
    z-index: 2;
    font-size: 16px;
  }
  .potenziamenti {
    grid-area: potenziamenti;
    position: relative;
  }
  .potenziamenti img {
    width: 98%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
  }
  .potenziamenti .valore {
    color: white;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -36%);
    z-index: 2;
    font-size: 18px;
  }
  .carta:hover {
    transform: scale(1.2);
    position: relative;
    z-index: 20;
    box-shadow: #00000070 -1px 8px 10px 0px;
  }
</style>
