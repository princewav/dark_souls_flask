<script>
  import { range } from '../utils.js';
  import { fade } from 'svelte/transition';

  let caselle = range(10).map(i => '');

  function update(i) {
    if (caselle[i] === 'energia' && (!caselle[i + 1] || caselle[i + 1] === 'salute'))
      caselle[i] = '';
    else if (caselle[i] === 'salute' && (!caselle[i - 1] || caselle[i - 1] === 'energia'))
      caselle[i] = '';
    else if (i === 0 || caselle[i - 1] === 'energia') caselle[i] = 'energia';
    else if (i === 9 || caselle[i + 1] === 'salute') caselle[i] = 'salute';
  }
</script>

<div class="lifebar">
  {#each caselle as casella, i}
    <div class="casella" on:click={() => update(i)}>
      <div class="q {casella}" />
    </div>
  {/each}
</div>

<style>
  .lifebar {
    position: relative;
    user-select: none;
    display: flex;
    justify-content: space-evenly;
    margin-top: 10px;
    background: linear-gradient(45deg, black, brown);
    padding: 10px 0px;
    border: 3px solid #85542f;
    box-sizing: border-box;
    border-radius: 6px;
  }

  .casella {
    width: 42px;
    height: 42px;
    background: #ffffff29;
    box-shadow: inset 0 0 12px 2px #ffffff59;
    transition: all 0.5s ease;
  }

  .casella:hover {
    background: #ffd49334;
  }

  .q {
    width: 36px;
    height: 36px;
    margin-top: 3px;
    margin-left: 3px;
    transition: all 0.2s ease;
    border-radius: 5px;
    box-shadow: 0 0 12px 2px #00000059;
  }
  .q:hover {
    transform: scale(1.1);
  }

  .salute {
    background: linear-gradient(-145deg, #b50000, #2d1717);
  }
  .energia {
    background: linear-gradient(-145deg, black, #0000007a);
  }

  .hidden {
    display: none;
  }
</style>
