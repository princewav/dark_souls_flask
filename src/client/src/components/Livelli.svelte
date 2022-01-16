<script>
  let headers = ['', 'BASE', 'TIER 1', 'TIER 2', 'TIER 3'];
  let stats = [
    { name: 'forza', levels: [[16, 1], [23, 0], [32, 0], [40, 0]] },
    { name: 'destrezza', levels: [[9, 1], [16, 0], [25, 0], [35, 0]] },
    { name: 'intelligenza', levels: [[8, 1], [15, 0], [23, 0], [30, 0]] },
    { name: 'fede', levels: [[9, 1], [16, 0], [25, 0], [35, 0]] }
  ];

  function upgrade(stat, i) {
    let curr = stat.levels[i];
    if ((i === 3 && stat.levels[2][1]) || (!stat.levels[i + 1][1] && stat.levels[i - 1][1]))
      stat.levels[i] = [curr[0], !curr[1]];

    stats = stats;
  }
</script>

<table>
  <tr>
    {#each headers as header}
      <th>{header}</th>
    {/each}
  </tr>
  {#each stats as stat}
    <tr>
      <td>
        <img src="images/simbolo-{stat.name}.png" alt={stat.name} />
        {stat.name.toUpperCase()}
      </td>
      {#each stat.levels as [level, upgraded], i}
        <td class:upgraded on:click={() => upgrade(stat, i)}>{level}</td>
      {/each}
    </tr>
  {/each}
</table>

<style>
  table {
    background: rgba(255, 255, 255, 0.644);
    height: 330px;
    font-size: 26px;
    text-align: center;
    border: #85542f 2px solid;
    width: 100%;
    user-select: none;
    border-spacing: 0;
    border-radius: 6px;
  }

  td,
  th {
    border: #85542f 1px solid;
    vertical-align: middle;
    transition: all 0.5s ease;
    width: 90px;
  }

  td:first-child {
    text-align: left;
    padding-left: 57px;
    font-weight: bold;
    position: relative;
    width: fit-content;
  }

  .upgraded {
    background: rgb(183, 158, 112);
  }

  td:not(.upgraded):hover {
    background: rgba(245, 222, 179, 0.479);
  }

  td img {
    width: 42px;
    position: absolute;
    top: 9px;
    left: 8px;
  }
</style>
