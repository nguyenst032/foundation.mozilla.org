let shell = require(`shelljs`);

let runDeploy = (remote) => {
  shell.echo(`Running deployment now...`);

  shell.exec(`npm run build`);

  shell.echo(`${new Date}\n\n\n`).to(`last-built.txt`);
  shell.exec(`git log -n 1 >> last-built.txt`);

  shell.exec(`git branch -D gh-pages`);
  shell.exec(`git checkout --orphan gh-pages`);

  shell.rm(`.gitignore`);

  shell.echo(`/*\n`).toEnd(`.gitignore`);

  let whitelist = shell.ls(`dest`);

  whitelist.forEach((item) => {
    shell.echo(`!${item}\n`).toEnd(`.gitignore`);
  });

  shell.echo(`!last-built.txt\n`).toEnd(`.gitignore`);

  shell.mv(`dest/*`, `./`);

  shell.exec(`git reset`);
  shell.exec(`git add .`);
  shell.exec(`git commit -m 'Deployed via stage.js script'`);
  shell.exec(`git push ${remote} gh-pages -f`);

  shell.echo(`Finished deploying!`);
};

// Check for remote argument
if (process.argv[2]) {
  runDeploy(process.argv[2]);
} else {
  shell.echo(`Missing target remote!`);
  shell.exit(2);
}
