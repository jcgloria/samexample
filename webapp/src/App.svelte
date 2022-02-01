<script>
	let url = "https://asd.execute-api.us-east-1.amazonaws.com" // Indicate API URL
	let email;
	let name;
	let age;
	let empleados = fetchData();
	function refresh() {
		empleados = fetchData();
	}
	async function fetchData() {
		const response = await fetch(
			url + "/items" 
		);
		return await response.json();
	}
	async function doPost() {
		const res = await fetch(
			url + "/items", 
			{
				method: "POST",
				body: JSON.stringify({
					email: email,
					name: name,
					age: age,
				}),
			}
		);
		const json = await res.json();
		if (json["ResponseMetadata"]["HTTPStatusCode"] == 200) {
			console.log("OK");
			refresh();
			email = "";
			name = "";
			age = "";
		} else {
			console.log(json);
		}
	}
</script>

<main>
	{#await empleados}
		<p>Cargando...</p>
	{:then empleados}
		<div class="container" style="margin-top: 1%;">
			<div>
				<div class="input-group mb-3">
					<input
						bind:value={email}
						type="text"
						class="form-control"
						placeholder="Correo"
						aria-label="Correo"
						aria-describedby="basic-addon1"
					/>
					<input
						bind:value={name}
						type="text"
						class="form-control"
						placeholder="Nombre"
						aria-label="Nombre"
						aria-describedby="basic-addon1"
					/>
					<input
						bind:value={age}
						type="text"
						class="form-control"
						placeholder="Edad"
						aria-label="Edad"
						aria-describedby="basic-addon1"
					/>
					<button
						on:click={doPost}
						type="button"
						class="btn btn-success">Agregar</button
					>
				</div>
			</div>
			<table class="table">
				<thead>
					<tr>
						<th scope="col">Correo</th>
						<th scope="col">Nombre</th>
						<th scope="col">Edad</th>
					</tr>
				</thead>
				<tbody>
					{#each empleados as empleado (empleado.email)}
						<tr>
							<td>{empleado.email}</td>
							<td>{empleado.name}</td>
							<td>{empleado.age}</td>
						</tr>
					{/each}
				</tbody>
			</table>
		</div>
	{/await}
</main>
